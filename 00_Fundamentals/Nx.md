# Nx 学习手册

> 目标：从几乎零基础出发，最终能够看懂、运行、修改、维护 Nx 项目。

## 目录

- [01-Nx是什么](#01-nx是什么)
- [02-Monorepo与Workspace](#02-monorepo与workspace)
- [03-Nx项目结构](#03-nx项目结构)
- [04-Project-Target-Task-Executor](#04-project-target-task-executor)
- [05-nxjson与projectjson](#05-nxjson与projectjson)
- [06-Nx-CLI](#06-nx-cli)
- [07-Project-Graph与Task-Graph](#07-project-graph与task-graph)
- [08-Cache与Affected](#08-cache与affected)
- [09-Generators与Plugins](#09-generators与plugins)

---

## 01-Nx是什么

### 1.1 一句话理解
Nx 是一个面向 Monorepo 的工程化工具链，核心能力是：

- 统一管理多项目（前端、后端、库）
- 通过依赖图精确执行任务
- 利用本地/远程缓存显著加速 CI
- 提供生成器和插件体系，降低维护成本

### 1.2 它解决什么问题

没有 Nx 时，常见痛点：

- 项目多了以后命令分散、脚本重复
- 不知道改动影响了哪些应用
- CI 全量构建/测试太慢
- 团队规范难统一

Nx 的对应方案：

- 统一入口：`nx <target> <project>`
- 依赖感知：Affected 只跑受影响部分
- 任务缓存：同样输入直接复用历史结果
- 代码生成：Generator 生成规范化代码与配置

### 1.3 你先记住的三个关键词

- Project：应用或库
- Target：项目可执行动作（build/test/lint 等）
- Cache：任务结果可复用

---

## 02-Monorepo与Workspace

### 2.1 Monorepo 是什么

Monorepo：多个项目放在同一个仓库里统一管理。

典型场景：

- `apps/` 放多个应用
- `libs/` 放可复用库
- 所有项目共享一套工具链和规范

### 2.2 Workspace 是什么

在 Nx 语境里，Workspace 就是整个 Nx 工作区（仓库根目录）。

你可以把它理解成：

- 一个大的工程容器
- 里面包含多个 Project
- 有统一的配置文件（如 `nx.json`）

### 2.3 Monorepo 的收益与代价

收益：

- 代码复用和协作效率高
- 依赖管理集中
- 改动影响分析准确

代价：

- 学习成本更高
- 配置理解要求更强

你现在的学习目标就是把“代价”降下来。

---

## 03-Nx项目结构

### 3.1 常见目录结构

```text
myorg/
	apps/
		web/
		api/
	libs/
		ui/
		utils/
	nx.json
	package.json
	tsconfig.base.json
```

### 3.2 核心结构说明

- `apps/`：可部署应用（如 React/Node 服务）
- `libs/`：共享库（工具函数、UI 组件、业务 SDK）
- `nx.json`：Nx 全局行为配置
- `project.json`：单个项目配置（常在项目目录下）
- `package.json`：依赖和脚本

### 3.3 你读项目时的顺序

建议固定流程：

1. 看 `nx.json`：了解全局规则
2. 找目标项目的 `project.json`：看有哪些 target
3. 执行 `nx show project <项目名>`：快速确认配置
4. 再看源码：知道入口和依赖

---

## 04-Project-Target-Task-Executor

### 4.1 概念关系

- Project：项目（例如 `web`）
- Target：动作名称（例如 `build`）
- Task：一次具体执行（例如在当前分支执行 `web:build`）
- Executor：实际执行器（例如 webpack、vite、jest 对应的 Nx executor）

可以理解为：

`Project + Target + 参数 => Task，由 Executor 执行`

### 4.2 示例

```json
{
	"name": "web",
	"targets": {
		"build": {
			"executor": "@nx/vite:build",
			"options": {
				"outputPath": "dist/apps/web"
			}
		}
	}
}
```

上面表示：

- 项目 `web` 有个 `build` 目标
- 执行时用 `@nx/vite:build`
- 输出目录是 `dist/apps/web`

### 4.3 常见 target

- `build`：构建
- `serve`：本地启动
- `test`：单元测试
- `lint`：代码检查
- `e2e`：端到端测试

---

## 05-nxjson与projectjson

> 你给的标题里是 `project.jsmd`，在 Nx 中通常是 `project.json`。

### 5.1 nx.json 做什么

`nx.json` 负责全局配置，常见内容：

- 默认任务选项（`targetDefaults`）
- 缓存相关配置
- 输入输出声明（影响缓存命中）
- 插件声明

示例（简化）：

```json
{
	"targetDefaults": {
		"build": {
			"dependsOn": ["^build"],
			"cache": true
		},
		"test": {
			"cache": true
		}
	}
}
```

### 5.2 project.json 做什么

`project.json` 负责单项目配置，主要定义：

- `name`
- `sourceRoot`
- `projectType`（application/library）
- `targets`（每个 target 的 executor/options/configurations）

### 5.3 两者分工

- `nx.json`：全局“公司制度”
- `project.json`：项目“具体执行细则”

---

## 06-Nx-CLI

### 6.1 最常用命令

```bash
# 查看工作区所有项目
nx show projects

# 查看某个项目配置
nx show project web

# 运行目标任务
nx run web:build

# 运行多个项目同一目标
nx run-many -t test -p web,api

# 运行受影响项目任务
nx affected -t build

# 打开依赖图
nx graph
```

### 6.2 推荐你先练的命令路线

1. `nx show projects`
2. `nx show project <任一项目>`
3. `nx run <项目>:build`
4. `nx run <项目>:test`
5. `nx graph`
6. `nx affected -t build`

练完这 6 步，你就能独立“读+跑”大多数 Nx 项目。

### 6.3 日常排错命令

```bash
# 详细日志
nx run web:build --verbose

# 忽略缓存，强制重跑
nx run web:test --skip-nx-cache

# 重置本地 Nx 状态与缓存
nx reset
```

---

## 07-Project-Graph与Task-Graph

### 7.1 Project Graph（项目依赖图）

Project Graph 关注“谁依赖谁”：

- `web` 依赖 `ui`
- `ui` 依赖 `utils`

它回答：改了一个库，会影响哪些项目？

### 7.2 Task Graph（任务依赖图）

Task Graph 关注“任务执行顺序”：

- `web:build` 前要先跑 `ui:build`
- `ui:build` 前要先跑 `utils:build`

它回答：这些任务应如何并行/串行执行？

### 7.3 为什么你必须理解这两个图

因为 Nx 的性能优化（Affected、Cache、并行调度）都建立在“图”上。

---

## 08-Cache与Affected

### 8.1 Cache 是什么

当任务输入不变时，Nx 直接复用历史结果，不再重复执行。

输入通常包括：

- 源代码
- 配置文件
- 依赖版本
- 命令参数

### 8.2 Affected 是什么

Affected 根据 Git 改动和依赖图，找出受影响项目，只跑必要任务。

常见命令：

```bash
nx affected -t test
nx affected -t build
nx affected -t lint
```

在 CI 中常见形式：

```bash
nx affected -t test --base=origin/main --head=HEAD
```

### 8.3 维护者视角的价值

- 提速：减少无效构建与测试
- 稳定：减少偶发问题面
- 可预测：改动影响范围可视化

---

## 09-Generators与Plugins

### 9.1 Generator 是什么

Generator 是代码和配置脚手架。

它可以：

- 生成新应用/库
- 自动改配置
- 按团队约定产出目录与模板

示例：

```bash
nx g @nx/react:app admin
nx g @nx/js:lib shared-utils
```

### 9.2 Plugin 是什么

Plugin 是 Nx 扩展机制，提供：

- Executors（如何执行任务）
- Generators（如何生成代码）
- 对特定技术栈的集成能力

### 9.3 维护阶段你会怎么用

- 统一新项目创建流程（Generator）
- 封装组织内规范（内部 Plugin）
- 让项目迭代时减少“手工改配置”

---

## 从“知道”到“会维护”的实战学习路径

### 第 1 阶段（1-2 天）：会读、会跑

1. 在任意 Nx 仓库执行：`nx show projects`
2. 选 1 个 app，执行：`nx show project <app>`
3. 运行 `build/test/lint`
4. 打开图：`nx graph`

达成标准：你能解释某个项目为什么能跑起来。

### 第 2 阶段（2-4 天）：会改

1. 新建 1 个 lib
2. 在 app 中引用它
3. 增加一个 target（比如自定义脚本）
4. 跑 `nx affected -t test` 验证影响范围

达成标准：你能安全改功能并验证影响。

### 第 3 阶段（持续）：会维护

1. 优化 `targetDefaults`
2. 在 CI 接入 affected + cache
3. 用 Generator 固化团队模板

达成标准：你能让团队交付更快、更稳。

---

## 常见坑位速查

- 命令能跑但很慢：先看是否命中缓存（必要时加 `--verbose`）
- 改了一个库导致很多任务执行：检查依赖边是否过宽
- target 配置不生效：确认是在正确项目的 `project.json`
- CI 和本地结果不一致：检查 `base/head`、Node 版本、锁文件

---

## 你下一步可以立即做的事

1. 找一个真实 Nx 仓库，按“第 1 阶段”完整跑一遍。
2. 把你跑命令时遇到的报错贴出来，我可以带你逐条定位。
3. 如果你愿意，我下一版可以给你做一份“从 0 创建 Nx Workspace 到接入 CI 缓存”的实战教程。
