

# [SUCTF 2019]CheckIn

1. 打开是一个上传表单

   ![image-20211011144044700](https://i.loli.net/2021/10/11/DOEunBKyfx2oacV.png)

   

2. 尝试上传一个图片马，发现过滤`<?`

![image-20211011144441883](https://i.loli.net/2021/10/11/NGUp1Wn4xfwcRlH.png)



3. 使用script脚本形式绕过

![image-20211011153916504](https://i.loli.net/2021/10/11/bwi7nZdle6NzARI.png)



4. 上传一个**.user.ini**

如果访问当前目录下的其它php文件，会自动包含**11.gif**

```ini
GIF89a
auto_prepend_file=11.gif
```

![image-20211011154042445](https://i.loli.net/2021/10/11/SgdbzrIjM39NfKp.png)



5. 访问上传目录下的index.php

![image-20211011154004266](https://i.loli.net/2021/10/11/i3nCG6O5Mx7j8Fb.png)



Get Flag！