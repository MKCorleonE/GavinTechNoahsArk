# Order Router：三个脚本的缺陷与修改分析

> 本文依据题目截图中的客户投诉、三份原始脚本及老师给出的修改方案整理。结论应在正式环境中结合完整测试、模型定义和迁移记录验证。

## 一、问题与代码文件对应关系

| 客户问题 | 对应文件 | 核心缺陷 |
| --- | --- | --- |
| 已送达订单仍显示为 Pending | `app/orders.py` | 使用 `fulfilled_at` 是否为空推断订单状态，未正确兼容历史迁移数据 |
| 部分订单没有确认邮件 | `app/notifications.py` | 捕获所有异常并静默返回 `False`，使网络故障不可见 |
| 闪购时库存变为负数 | `app/inventory.py` | 先查询／检查、后扣减，存在并发竞争窗口 |

---

## 二、`app/orders.py`：已送达订单仍显示 Pending

### 客户现象

三月平台迁移前下单的部分订单已经送达，但订单后台仍显示为 `Pending`。近期订单没有同类问题。

### 原始代码

```python
from datetime import datetime
from typing import List

from sqlalchemy.orm import Session

from .models import Order


def get_pending_orders(session: Session) -> List[Order]:
    """Return all orders that are still awaiting fulfillment."""
    return session.query(Order).filter(Order.fulfilled_at == None).all()


def create_order(session: Session, customer_id: int, product_id: int, qty: int) -> Order:
    """Create a new order in PENDING state and persist it."""
    order = Order(
        customer_id=customer_id,
        product_id=product_id,
        quantity=qty,
        status="PENDING",
    )
    session.add(order)
    session.commit()
    session.refresh(order)
    return order


def fulfill_order(session: Session, order_id: int) -> bool:
    """Mark an order FULFILLED and timestamp. Returns False if not found."""
    order = session.query(Order).filter_by(id=order_id).first()
    if order is None:
        return False

    order.status = "FULFILLED"
    order.fulfilled_at = datetime.utcnow()
    session.commit()
    return True
```

### 根因分析

`get_pending_orders` 使用 `fulfilled_at == None` 判断订单是否待处理。对于新订单，完成订单时会同时写入 `status = "FULFILLED"` 和 `fulfilled_at`，此判断通常可用。

但投诉明确指出问题只影响迁移前的旧订单。合理推断是：部分历史订单虽已送达或已有非 Pending 状态，却没有正确填充 `fulfilled_at`。这样它们会被错误查询为待处理订单。

### 建议修改

应使用业务状态字段判断，而不是以时间字段推断状态：

```python
def get_pending_orders(session: Session) -> List[Order]:
    """Return all orders that are still awaiting fulfillment."""
    return session.query(Order).filter(Order.status == "PENDING").all()
```

### 为什么正确

- `status` 是订单生命周期的明确业务来源；
- `fulfilled_at` 是完成时间的辅助记录，不应单独决定订单状态；
- 历史订单即使缺少完成时间，只要状态不为 `PENDING` 就不会错误显示在待处理列表中。

### 与老师方案对比

老师的修改点 1 同样将查询改为：

```python
return session.query(Order).filter(Order.status == "PENDING").all()
```

结论：一致。

---

## 三、`app/notifications.py`：确认邮件有时没有发送

### 客户现象

部分客户没有收到送达确认邮件。通知服务仪表盘中没有这些订单的入站请求，应用日志也没有报错。

### 原始代码

```python
import logging

import requests

logger = logging.getLogger(__name__)

NOTIFY_URL = "http://notification-service/notify"

# Module-level client — exposed so tests can monkeypatch without reimporting.
http_client = requests.Session()


def notify_customer(order_id: int, email: str) -> bool:
    """
    POST an order-confirmation event to the notification microservice.

    Returns True when the service acknowledges the request (2xx).
    Returns False when the service responds with a non-2xx status code.
    """
    try:
        resp = http_client.post(
            NOTIFY_URL,
            json={"order_id": order_id, "email": email},
            timeout=5,
        )
        resp.raise_for_status()
        return True
    except Exception:
        return False
```

### 根因分析

函数文档约定：通知服务响应非 2xx 时返回 `False`。但 `except Exception` 会捕获远多于 HTTP 非成功响应的异常，包括：

- 连接失败；
- 超时；
- DNS 解析失败；
- 代码本身的编程错误。

这些异常被转换为普通的 `False`，且代码没有记录日志。于是上层可能无法触发异常处理、重试或告警，造成“通知服务没有收到请求、应用日志也没有错误”的现象。

### 建议修改

只捕获 `raise_for_status()` 在收到非 2xx HTTP 响应时抛出的异常：

```python
def notify_customer(order_id: int, email: str) -> bool:
    try:
        resp = http_client.post(
            NOTIFY_URL,
            json={"order_id": order_id, "email": email},
            timeout=5,
        )
        resp.raise_for_status()
        return True
    except requests.exceptions.HTTPError:
        return False
```

### 为什么正确

- 通知服务明确返回 4xx / 5xx 时，`raise_for_status()` 抛出 `HTTPError`，函数按约定返回 `False`；
- 网络连接或超时问题不再被静默吞掉，而是向上抛出；
- 上层调用者因而可以记录错误、触发重试或将任务标记为失败。

### 需要谨慎说明的地方

题目截图没有展示调用 `notify_customer` 的上层订单流程。因此，不能只凭这三个文件断言“异常向上抛出后一定会自动重试”。能确定的是：原代码掩盖了网络层异常；缩小捕获范围后，故障将变得可见，并可由调用方处理。

### 与老师方案对比

老师的修改点 2 是：

```python
except requests.exceptions.HTTPError:
    return False
```

结论：一致。

---

## 四、`app/inventory.py`：高并发下库存为负数

### 客户现象

闪购期间，约有 40～80 个并发结账请求。部分商品库存最终显示为负数，导致超卖和取消订单；低流量下不容易复现。

### 原始代码

```python
from sqlalchemy.orm import Session

from .models import Inventory


def reserve_stock(session: Session, product_id: int, qty: int) -> bool:
    """
    Reserve ``qty`` units of ``product_id`` from inventory.

    Returns True if the reservation succeeded, False if stock is insufficient
    or the product is unknown.
    """
    row = session.query(Inventory).filter_by(product_id=product_id).first()
    if row is None or row.stock < qty:
        return False

    row.stock -= qty
    session.commit()
    return True


def release_stock(session: Session, product_id: int, qty: int) -> None:
    """Return ``qty`` units to inventory (e.g. after a cancelled order)."""
    row = session.query(Inventory).filter_by(product_id=product_id).first()
    if row is not None:
        row.stock += qty
        session.commit()


def get_stock_level(session: Session, product_id: int) -> int:
    """Return current stock level, or 0 if the product is not in inventory."""
    row = session.query(Inventory).filter_by(product_id=product_id).first()
    return row.stock if row is not None else 0
```

### 根因分析

`reserve_stock` 将流程拆为多个独立步骤：

```text
查询库存 → 判断库存是否足够 → 在 Python 内存中扣减 → 提交事务
```

高并发时，多个请求可以同时在扣减前读取同一个旧库存值并各自通过检查。这是典型的“检查后再执行”（TOCTOU）竞争条件。

示例：库存为 1，两个请求各购买 1 件。

```text
请求 A：读取库存 1
请求 B：读取库存 1
请求 A：判断 1 >= 1，允许购买
请求 B：判断 1 >= 1，允许购买
请求 A / B：分别扣减并提交
```

系统可能超卖，具体结果依赖数据库隔离级别、SQLAlchemy 会话与写入时序；题目投诉已表明生产中可能出现负库存。

### 建议修改：条件原子更新

将“库存足够”和“扣减库存”放进同一条数据库更新语句：

```python
def reserve_stock(session: Session, product_id: int, qty: int) -> bool:
    updated = (
        session.query(Inventory)
        .filter(
            Inventory.product_id == product_id,
            Inventory.stock >= qty,
        )
        .update(
            {Inventory.stock: Inventory.stock - qty},
            synchronize_session=False,
        )
    )

    if updated == 0:
        return False

    session.commit()
    return True
```

`updated` 是实际受影响的行数：

- 商品不存在：更新 0 行，返回 `False`；
- 商品库存不足：更新 0 行，返回 `False`；
- 商品存在且库存充足：更新 1 行，提交并返回 `True`。

这样数据库不会扣减任何不满足 `stock >= qty` 条件的记录，库存判断和扣减具有原子性。

### `release_stock` 的对应修改

虽然释放库存通常不会导致负库存，但同样可采用数据库表达式更新，避免“先读取，再在 Python 中加库存”的并发丢失更新风险：

```python
def release_stock(session: Session, product_id: int, qty: int) -> None:
    updated = (
        session.query(Inventory)
        .filter(Inventory.product_id == product_id)
        .update(
            {Inventory.stock: Inventory.stock + qty},
            synchronize_session=False,
        )
    )

    if updated:
        session.commit()
```

### 与老师方案对比

老师的修改点 3 也采用：

- `Inventory.stock >= qty` 作为更新条件；
- `Inventory.stock - qty` 作为数据库端更新表达式；
- 根据受影响行数判断预留是否成功；
- `release_stock` 使用 `Inventory.stock + qty` 的数据库端更新。

结论：一致。

### 可额外检查的边界条件

截图未说明 `qty` 是否保证为正数。若题目没有此约束，生产代码还应拒绝 `qty <= 0`，因为负数“预留”会反向增加库存。但若题目或测试已保证数量为正，则不应无故扩大本题修改范围。

---

## 五、提交前检查清单

- [ ] 待处理订单只由 `status == "PENDING"` 决定；
- [ ] 通知函数不会吞掉网络异常或编程错误；
- [ ] HTTP 非 2xx 响应仍按函数约定返回 `False`；
- [ ] 库存预留使用带 `stock >= qty` 条件的单条更新；
- [ ] 根据更新行数判断商品是否存在、库存是否足够；
- [ ] 库存释放不会因读—改—写造成并发丢失更新；
- [ ] 没有修改题目规定以外的文件；
- [ ] 没有使用固定订单号、商品号或测试数据进行硬编码；
- [ ] 已运行 `pytest tests/ -v --tb=short`；
- [ ] `root_cause_note.md` 解释了根因、影响和修复原则，而不只是列出代码改动。

