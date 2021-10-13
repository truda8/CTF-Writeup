# [MRCTF2020]你传你🐎呢

1. 打开是上传表单

![image-20211012102400809](https://i.loli.net/2021/10/12/96QSf4xoMekAjNp.png)



2. 上传测试

- 不能上传gif图片
- 可以上传jpg图片
- 没有进行内容检测
- 上传后可以得到文件的绝对路径

![image-20211012103017329](https://i.loli.net/2021/10/12/Shkr97idu6XV4Ka.png)

- 校验方式为黑名单

![image-20211012103301689](https://i.loli.net/2021/10/12/YG7dF39JoKuhIeq.png)



3. 尝试上传.htaccess成功

```
// 表示把jpg当作php执行
AddType   application/x-httpd-php   .jpg
```

![image-20211012105617626](https://i.loli.net/2021/10/12/Wdxk1fSQ6TqZDIH.png)



5. 再上传一个图片马

![image-20211012105719888](https://i.loli.net/2021/10/12/uoE6GcQYRarhXq5.png)



6. 蚁剑连接Get Flag

![image-20211012105538635](https://i.loli.net/2021/10/12/OVEqeuIv1pUti8r.png)



