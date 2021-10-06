# [极客大挑战 2019]Havefun

查看网页源代码，发现注释的PHP代码：
```php
$cat=$_GET['cat'];
echo $cat;
if($cat=='dog'){
    echo 'Syc{cat_cat_cat_cat}';
}
```

构造URL：`http://xxx.xxx.xxx/?cat=dog`，直接get flag.