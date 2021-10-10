# notrequired

## 1. 基础判断

打开会自动跳转到`/index.php?file=index.html`

尝试**任意文件读取**，成功读取 `/etc/passwd`

![image-20211009152022188](https://i.loli.net/2021/10/09/qQJvfUmPgX9o8lI.png)



## 2. 读取文件

使用`php://filter`过滤器读取index.php的base64编码字符串

![image-20211009152211244](https://i.loli.net/2021/10/09/Jkvm2FrOPKGqxn4.png)

解码得到：

```php
<?php

if(!isset($_GET["file"])){
    header("location: http://ctf.bennetthackingcommunity.cf:8333/index.php?file=index.html");
    exit;
}

else{
    require($_GET['file']);
}

#note to myself: delete /bin/secrets.txt!
?>
```



根据提示，读取 **/bin/secrets.txt**

![image-20211009152437906](https://i.loli.net/2021/10/09/qf2Q8bUpXioTvgE.png)

把**BUHC**替换为**DO**即为Flag。



Get Flag!

