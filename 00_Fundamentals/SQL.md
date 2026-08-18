# SQL 学习手册（简体中文版）

## 目录
- [1 SQL 简介](#1-sql-简介)
  - [1.1 SQL是什么?](#11-sql是什么)
  - [1.2 SQL 能做什么？](#12-ql-能做什么)
- [2 SQL 语法引言](#sql-语法引言)
  - [2.1 数据库表](#21-数据库表)
  - [2.2 关于大小写](#22-关于大小写)
  - [2.3 关于分号结尾](#23-关于分号结尾)
- [3 SQL 语句](#sql-语句)
  - [3.1 SELECT 语句](#31-select-语句)
  - [3.2 SELECT DISTINCT 语句](#32-select-distinct-语句)
  - [3.3 INSERT INTO 语句](#33-insert-into-语句)
  - [3.4 UPDATE 语句](#34-update-语句)
  - [3.5 DELETE 语句](#35-delete-语句)
- [4 SQL 数据类型](#sql-数据类型)

## 1 SQL 简介
> SQL (Structured Query Language:结构化查询语言) 是用于管理关系数据库管理系统（RDBMS）。SQL 通过一系列的语句和命令来执行数据定义、数据查询、数据操作和数据控制等功能,包括数据插入、查询、更新和删除，数据库模式创建和修改，以及数据访问控制。

### 1.1 SQL是什么?
- SQL 指结构化查询语言，全称是 Structured Query Language。
- SQL 让您可以访问和处理数据库，包括数据插入、查询、更新和删除。
- SQL 语言采用英语关键词，使其易读易写。
- SQL 由国际标准化组织（ISO）和美国国家标准协会（ANSI）标准化。
- SQL 提供了丰富的操作数据的功能，从简单的查询到复杂的数据库管理操作。

### 1.2 SQL 能做什么？
- SQL 面向数据库执行查询
- SQL 可从数据库取回数据
- SQL 可在数据库中插入新的记录
- SQL 可更新数据库中的数据
- SQL 可从数据库删除记录
- SQL 可创建新数据库
- SQL 可在数据库中创建新表
- SQL 可在数据库中创建存储过程
- SQL 可在数据库中创建视图
- SQL 可以设置表、存储过程和视图的权限

### RDBMS
>RDBMS 指关系型数据库管理系统，全称 Relational Database Management System。
RDBMS 是 SQL 的基础，同样也是所有现代数据库系统的基础，比如 MS SQL Server、IBM DB2、Oracle、MySQL 以及 Microsoft Access。RDBMS 中的数据存储在被称为表的数据库对象中。表是相关的数据项的集合，它由列和行组成。

## 2 SQL 语法引言
> SQL（Structured Query Language）是一种用于管理和操作关系数据库的标准语言，包括数据查询、数据插入、数据更新、数据删除、数据库结构创建和修改等功能。

| SQL 核心分类       | 语句                     |
|--------------------|------------------------------|
| 性能优化与安全性   | EXPLAIN、TRANSACTION、GRANT、REVOKE |
| 基本查询语句       | SELECT、WHERE、ORDER BY、DISTINCT、LIMIT |
| 表操作语句         | CREATE TABLE、ALTER TABLE、DROP TABLE |
| 高级操作           | UNION、CASE、INDEX           |
| 数据操作语句       | INSERT INTO、UPDATE、DELETE  |
| 函数与聚合操作     | COUNT、SUM、AVG、MIN、MAX    |
| 子查询与联接       | INNER JOIN、LEFT JOIN、RIGHT JOIN、FULL JOIN、SUBQUERY |


### 2.1 数据库表
一个数据库通常包含一个或多个表，每个表有一个名字标识（例如:"Websites"），表包含带有数据的记录（行）。在本教程中，我们在 MySQL 的 RUNOOB 数据库中创建了 Websites 表，用于存储网站记录。我们可以通过以下命令查看 "Websites" 表的数据：
```sql
mysql> use RUNOOB;
Database changed

mysql> set names utf8;
Query OK, 0 rows affected (0.00 sec)

mysql> SELECT * FROM Websites;
+----+--------------+---------------------------+-------+---------+
| id | name         | url                       | alexa | country |
+----+--------------+---------------------------+-------+---------+
| 1  | Google       | https://www.google.cm/    | 1     | USA     |
| 2  | 淘宝          | https://www.taobao.com/   | 13    | CN      |
| 3  | 菜鸟教程      | http://www.runoob.com/    | 4689  | CN      |
| 4  | 微博          | http://weibo.com/         | 20    | CN      |
| 5  | Facebook     | https://www.facebook.com/ | 3     | USA     |
+----+--------------+---------------------------+-------+---------+
5 rows in set (0.01 sec)
```
> - use RUNOOB; 命令用于选择数据库。
> - set names utf8; 命令用于设置使用的字符集。
> - SELECT * FROM Websites; 读取数据表的信息。
> - 上面的表包含五条记录（每一条对应一个网站信息）和5个列（id、name、url、alexa 和country）。

### 2.2 关于大小写
SQL 对大小写不敏感：SELECT 与 select 是相同的。

### 2.3 关于分号结尾
某些数据库系统要求在每条 SQL 语句的末端使用分号。分号是在数据库系统中分隔每条 SQL 语句的标准方法，这样就可以在对服务器的相同请求中执行一条以上的 SQL 语句。在本教程中，我们将在每条 SQL 语句的末端使用分号。

### 2.4 一些最重要的 SQL 命令
- SELECT - 从数据库中提取数据
- UPDATE - 更新数据库中的数据
- DELETE - 从数据库中删除数据
- INSERT INTO - 向数据库中插入新数据
- CREATE DATABASE - 创建新数据库
- ALTER DATABASE - 修改数据库
- CREATE TABLE - 创建新表
- ALTER TABLE - 变更（改变）数据库表
- DROP TABLE - 删除表
- CREATE INDEX - 创建索引（搜索键）
- DROP INDEX - 删除索引

## 3 SQL 语句
> SQL 语句是 SQL 的核心部分。SQL 语句用于执行各种操作，如查询数据、插入数据、更新数据和删除数据等。每条 SQL 语句都以分号（;）结尾。

### 3.1 SELECT 语句
```sql
SELECT column_name(s)
FROM table_name
WHERE condition
ORDER BY column_name [ASC|DESC]
```
**解析**
- column_name(s): 要查询的列。
- table_name: 要查询的表。
- condition: 查询条件（可选）。
- ORDER BY: 排序方式，ASC 表示升序，DESC 表示降序（可选）。

```sql
SELECT * FROM table_name;
```
从 table_name 表中选择所有列的数据。

```sql
SELECT * FROM Websites WHERE country='CN';
SELECT * FROM Websites WHERE id=1;
```
**文本字段 vs. 数值字段**
- SQL 使用单引号来环绕文本值（大部分数据库系统也接受双引号）。
- 在上个实例中 'CN' 文本字段使用了单引号。
- 如果是数值字段，请不要使用引号。

**WHERE 子句中的运算符**

| 运算符 | 描述 |
| :--- | :--- |
| = | 等于 |
| <> | 不等于。注释：在 SQL 的一些版本中，该操作符可被写成 != |
| > | 大于 |
| < | 小于 |
| >= | 大于等于 |
| <= | 小于等于 |
| BETWEEN | 在某个范围内 |
| LIKE | 搜索某种模式 |
| IN | 指定针对某个列的多个可能值 |

```sql
SELECT * FROM Websites
WHERE country='CN'
AND alexa > 50;

SELECT * FROM Websites
WHERE country='USA'
OR country='CN';

SELECT * FROM Websites
WHERE alexa > 15
AND (country='CN' OR country='USA');
```
**SQL AND & OR 运算符**
- 如果第一个条件和第二个条件都成立，则 AND 运算符显示一条记录。
- 如果第一个条件和第二个条件中只要有一个成立，则 OR 运算符显示一条记录。
- 二者可以结合使用，AND 运算符的优先级高于 OR 运算符。您可以使用括号来改变运算顺序。

### 3.2 SELECT DISTINCT 语句
```sql
SELECT DISTINCT column1, column2, ...
FROM table_name;
```
SELECT DISTINCT 语句用于返回唯一不同的值。在表中，一个列可能会包含多个重复值，有时您也许希望仅仅列出不同（distinct）的值。

### 3.3 INSERT INTO 语句
INSERT INTO 语句可以有两种编写形式。
第一种形式无需指定要插入数据的列名，只需提供被插入的值即可：
```sql
INSERT INTO table_name
VALUES (value1,value2,value3,...);
```
第二种形式需要指定列名及被插入的值：
```sql
INSERT INTO table_name (column1,column2,column3,...)
VALUES (value1,value2,value3,...);
```
**解析**
- table_name：需要插入新记录的表名。
- column1, column2, ...：需要插入的字段名。
- value1, value2, ...：需要插入的字段值。

**示例**
```sql
+----+--------------+---------------------------+-------+---------+
| id | name         | url                       | alexa | country |
+----+--------------+---------------------------+-------+---------+
| 1  | Google       | https://www.google.cm/    | 1     | USA     |
| 2  | 淘宝          | https://www.taobao.com/   | 13    | CN      |
| 3  | 菜鸟教程      | http://www.runoob.com/    | 4689  | CN      |
| 4  | 微博          | http://weibo.com/         | 20    | CN      |
| 5  | Facebook     | https://www.facebook.com/ | 3     | USA     |
+----+--------------+---------------------------+-------+---------+

INSERT INTO Websites (name, url, alexa, country)
VALUES ('百度','https://www.baidu.com/','4','CN');

+----+--------------+---------------------------+-------+---------+
| id | name         | url                       | alexa | country |
+----+--------------+---------------------------+-------+---------+
| 1  | Google       | https://www.google.cm/    | 1     | USA     |
| 2  | 淘宝          | https://www.taobao.com/   | 13    | CN      |
| 3  | 菜鸟教程      | http://www.runoob.com/    | 4689  | CN      |
| 4  | 微博          | http://weibo.com/         | 20    | CN      |
| 5  | Facebook     | https://www.facebook.com/ | 3     | USA     |
| 6  | 百度          | https://www.baidu.com/     | 4     | CN      |
+----+--------------+---------------------------+-------+---------+
```

### 3.4 UPDATE 语句
UPDATE 语句用于更新表中已存在的记录。
```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```
**解析**
- table_name：要修改的表名称。
- column1, column2, ...：要修改的字段名称，可以为多个字段。
- value1, value2, ...：要修改的值，可以为多个值。
- condition：修改条件，用于指定哪些数据要修改。

**示例**
```sql
+----+--------------+---------------------------+-------+---------+
| id | name         | url                       | alexa | country |
+----+--------------+---------------------------+-------+---------+
| 1  | Google       | https://www.google.cm/    | 1     | USA     |
| 2  | 淘宝          | https://www.taobao.com/   | 13    | CN      |
| 3  | 菜鸟教程      | http://www.runoob.com/    | 4689  | CN      |
| 4  | 微博          | http://weibo.com/         | 20    | CN      |
| 5  | Facebook     | https://www.facebook.com/ | 3     | USA     |
+----+--------------+---------------------------+-------+---------+

UPDATE Websites 
SET alexa='5000', country='USA' 
WHERE name='菜鸟教程';

+----+--------------+---------------------------+-------+---------+
| id | name         | url                       | alexa | country |
+----+--------------+---------------------------+-------+---------+
| 1  | Google       | https://www.google.cm/    | 1     | USA     |
| 2  | 淘宝          | https://www.taobao.com/   | 13    | CN      |
| 3  | 菜鸟教程      | http://www.runoob.com/    | 5000  | USA      |
| 4  | 微博          | http://weibo.com/         | 20    | CN      |
| 5  | Facebook     | https://www.facebook.com/ | 3     | USA     |
+----+--------------+---------------------------+-------+---------+

```

**Update 警告！**
在更新记录时要格外小心！在上面的实例中，如果我们省略了 WHERE 子句，如下所示：
```sql
UPDATE Websites
SET alexa='5000', country='USA'
```
执行以上代码会将 Websites 表中所有数据的 alexa 改为 5000，country 改为 USA。执行没有 WHERE 子句的 UPDATE 要慎重，再慎重。

### 3.5 DELETE 语句
DELETE 语句用于删除表中的行。
```sql
DELETE FROM table_name
WHERE condition;
```
**解析**
- table_name：要删除的表名称。
- condition：删除条件，用于指定哪些数据要删除。

**示例**
```sql
+----+--------------+---------------------------+-------+---------+
| id | name         | url                       | alexa | country |
+----+--------------+---------------------------+-------+---------+
| 1  | Google       | https://www.google.cm/    | 1     | USA     |
| 2  | 淘宝       | https://www.taobao.com/   | 13    | CN      |
| 3  | 菜鸟教程 | http://www.runoob.com/    | 4689  | CN      |
| 4  | 微博       | http://weibo.com/         | 20    | CN      |
| 5  | Facebook     | https://www.facebook.com/ | 3     | USA     |
+----+--------------+---------------------------+-------+---------+

DELETE FROM Websites
WHERE name='Facebook' AND country='USA';

+----+--------------+---------------------------+-------+---------+
| id | name         | url                       | alexa | country |
+----+--------------+---------------------------+-------+---------+
| 1  | Google       | https://www.google.cm/    | 1     | USA     |
| 2  | 淘宝       | https://www.taobao.com/   | 13    | CN      |
| 3  | 菜鸟教程 | http://www.runoob.com/    | 4689  | CN      |
| 4  | 微博       | http://weibo.com/         | 20    | CN      |
+----+--------------+---------------------------+-------+---------+
```

**删除所有数据**
您可以在不删除表的情况下，删除表中所有的行。这意味着表结构、属性、索引将保持不变：
```sql
DELETE FROM table_name;
```

### 3.6 ORDER BY 语句
- ORDER BY 关键字用于对结果集按照一个列或者多个列进行排序。
- ORDER BY 关键字默认按照升序对记录进行排序。如果需要按照降序对记录进行排序，您可以使用 DESC 关键字。
```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
```
**解析**
- column1, column2, ...：要排序的字段名称，可以为多个字段。
- ASC：表示按升序排序。
- DESC：表示按降序排序。

**示例**
```sql
+----+--------------+---------------------------+-------+---------+
| id | name         | url                       | alexa | country |
+----+--------------+---------------------------+-------+---------+
| 1  | Google       | https://www.google.cm/    | 1     | USA     |
| 2  | 淘宝          | https://www.taobao.com/   | 13    | CN      |
| 3  | 菜鸟教程      | http://www.runoob.com/    | 4689  | CN      |
| 4  | 微博          | http://weibo.com/         | 20    | CN      |
| 5  | Facebook     | https://www.facebook.com/ | 3     | USA     |
+----+--------------+---------------------------+-------+---------+

SELECT * FROM Websites
ORDER BY alexa;

+----+--------------+---------------------------+-------+---------+
| id | name         | url                       | alexa | country |
+----+--------------+---------------------------+-------+---------+
| 1  | Google       | https://www.google.cm/    | 1     | USA     |
| 5  | Facebook     | https://www.facebook.com/ | 3     | USA     |
| 2  | 淘宝          | https://www.taobao.com/   | 13    | CN      |
| 4  | 微博          | http://weibo.com/         | 20    | CN      |
| 3  | 菜鸟教程      | http://www.runoob.com/    | 4689  | CN      |

SELECT * FROM Websites
ORDER BY alexa DESC;

+----+--------------+---------------------------+-------+---------+
| id | name         | url                       | alexa | country |
+----+--------------+---------------------------+-------+---------+
| 3  | 菜鸟教程      | http://www.runoob.com/    | 4689  | CN      |
| 4  | 微博          | http://weibo.com/         | 20    | CN      |
| 2  | 淘宝          | https://www.taobao.com/   | 13    | CN      |
| 5  | Facebook     | https://www.facebook.com/ | 3     | USA     |
| 1  | Google       | https://www.google.cm/    | 1     | USA     |

SELECT * FROM Websites
ORDER BY country,alexa;

+----+--------------+---------------------------+-------+---------+
| id | name         | url                       | alexa | country |
+----+--------------+---------------------------+-------+---------+
| 2  | 淘宝          | https://www.taobao.com/   | 13    | CN      |
| 4  | 微博          | http://weibo.com/         | 20    | CN      |
| 3  | 菜鸟教程      | http://www.runoob.com/    | 4689  | CN      |
| 1  | Google       | https://www.google.cm/    | 1     | USA     |
| 5  | Facebook     | https://www.facebook.com/ | 3     | USA     |
```