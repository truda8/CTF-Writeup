# [HCTF 2018]admin

## 一、注册一个账号并登陆，查看源代码，发现提示

```
<!-- https://github.com/woadsl1234/hctf_flask/ -->
```



## 二、尝试伪造Session

参考：[客户端 session 导致的安全问题](https://www.leavesongs.com/PENETRATION/client-session-security.html)

1. 解密Session

2. 修改Session

3. 编码Session

![image-20211008191330987](https://i.loli.net/2021/10/08/BUCLmvYdnwMcNF7.png)



4. 复制到浏览器修改session，get flag!

![image-20211008191843769](https://i.loli.net/2021/10/08/VNauJ2wdLiUfBIG.png)

