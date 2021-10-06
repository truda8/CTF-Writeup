# [极客大挑战 2019]Upload

打开页面是一个图片上传的表单：

![image-20210927124052690](https://i.loli.net/2021/09/27/pEjKrtZANokTLMS.png)

尝试上传一张正常的图片，上传后返回文件名，但是不知道文件路径。

尝试扫描目录，发现一个*/upload/*目录，上传的文件都在这：

![image-20210927132447350](https://i.loli.net/2021/09/27/xWKqLEUgAT8Jbv6.png)

根据这个目录的文件判断，校验了文件头必须是GIF格式才能上传。

尝试抓包修改内容开头为**GIF89a**，图片上传成功！

![image-20210927133055281](https://i.loli.net/2021/09/27/ybTf6gG32EYD1wO.png)



把文件名称改为php后缀尝试上传，发现🚫禁止上传php后缀的文件：

![image-20210927133211837](https://i.loli.net/2021/09/27/uRCgf1hKdtNrwMe.png)



把后缀改为**.phtml**上传成功：

![image-20210927133627369](https://i.loli.net/2021/09/27/fPWIGQxSHZkKjcM.png)



修改内容，添加php代码，上传失败，提示内容不能包含“<?”

![image-20210927133756711](https://i.loli.net/2021/09/27/xtp6E13W9y7JDzX.png)

![image-20210927133745356](https://i.loli.net/2021/09/27/gO26odyJAQplfDK.png)



使用 **script php** 绕过，成功上传：

![image-20210927134105158](https://i.loli.net/2021/09/27/cUK8fXz3OAruwVH.png)



使用蚁剑连接，get flag!

