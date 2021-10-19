# **double sqli**

1. 修改`/?id=1`为`?id=2`，返回链接地址 `/files/test.jpg`
2. 直接访问 `/files/`，发现存开启了目录列表功能

![image-20211018185051441](https://i.loli.net/2021/10/18/ZrRJyPY4pIEMjoe.png)



3. Nginx 路径穿越

ClickHouse配置路径：`/etc/clickhouse-server/`

![image-20211018192200610](https://i.loli.net/2021/10/18/2wsH8NYQT94EA1k.png)

查看config.xml和users.xml，发现开启HTTP API接口，端口为8123

![image-20211018193608396](https://i.loli.net/2021/10/18/PZvKcS2g7F8Db4q.png)



ClickHouse 数据路径：var/lib/clickhouse/

![image-20211018193506786](https://i.loli.net/2021/10/18/6TYFcXtS5PpGZk9.png)



在 /var/lib/clickhouse/access/ 下发现sql文件

![image-20211018190344954](../../../../../../Users/apple/Library/Application Support/typora-user-images/image-20211018190344954.png)

下载下来，打开查看得到一个数据库用户和密码

- 用户名：user_01

- 密码：e3b0c44298fc1c149afb

![image-20211018190549423](../../../../../../Users/apple/Library/Application Support/typora-user-images/image-20211018190549423.png)



4. 利用注入点和HTTP API

利用以上获取的数据库用户名和密码，根据 ClickHouse 的 [url函数](https://clickhouse.com/docs/en/sql-reference/table-functions/url/) 和 [HTTP API](https://clickhouse.com/docs/en/interfaces/http/#cli-queries-with-parameters) 构造注入语句：

```sql
/?id=1 union all select html from url('http://localhost:8123/?user=user_01%26password=e3b0c44298fc1c149afb%26database=ctf%26query=select%2520*%2520from%2520flag',RawBLOB,'html String')
```

> 注意：URL函数里的url地址中的空格需要二次url编码



打开以上链接 Get flag：

![image-20211018195810065](https://i.loli.net/2021/10/18/j18B7FfiEpAPGXs.png)







