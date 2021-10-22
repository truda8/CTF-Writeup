# [GXYCTF2019]BabySQli

## 一、打开页面是一个登陆表单

![image-20211019192953409](https://i.loli.net/2021/10/19/1bWE2INrCjmq3TG.png)

发现页面存在注释信息，进行解码发现需要先base32解码然后再base64解码，得到内容：

```sql
select * from user where username = '$name'
```

![image-20211019202216878](https://i.loli.net/2021/10/19/vCna7smtTgPHJZX.png)





## 二、根据题目和页面提示进行注入测试

1. 加单引号报错，可知目标是 MySQL 数据库

![image-20211019193049383](https://i.loli.net/2021/10/19/lK6FwXSJghdpTL8.png)



2. 根据回显猜测出用户名为admin



3. 使用联合查询判断字段数，得到3

![image-20211020091707245](https://i.loli.net/2021/10/20/zBUTyfFnRCYjLaA.png)



3. 判断username位置

![image-20211020091859223](https://i.loli.net/2021/10/20/w1aZBirbOnX3kLA.png)



4. 自己构造一个md5(password)来登录

![image-20211020092136777](https://i.loli.net/2021/10/20/AMwTriY9b6K7ahs.png)



Get Flag！
