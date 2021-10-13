# [BJDCTF2020]Easy MD5

1. 打开页面有一个输入框

![image-20211010222703543](https://i.loli.net/2021/10/10/myxq3Za2XAhbSoV.png)



2. BurpSuite 抓包测试，得到提示

```SQL
select * from 'admin' where password=md5($pass,true)
```

![image-20211010224814146](https://i.loli.net/2021/10/10/dZQ39GAivK2Narq.png)



3. 绕过MD5函数

这个点的原理是 **ffifdyop** 这个字符串被 md5 哈希了之后会变成 276f722736c95d99e921722cf9ed621c，这个字符串前几位刚好是`'or '6`，而 Mysql 刚好又会吧 hex 转成 ascii 解释，因此拼接之后的形式是

```sql
select * from 'admin' where password='' or '6xxxxx'
```

等价于 or 一个永真式，因此相当于万能密码，可以绕过md5()函数。

![image-20211011131416965](https://i.loli.net/2021/10/11/ZNUQoRe14vTXsPB.png)

跳转地址：./levels91.php



4. 访问跳转地址，得到PHP代码片段

![image-20211011131513807](https://i.loli.net/2021/10/11/eLqlgMsGEVC3Wn1.png)

```php
<!--
$a = $GET['a'];
$b = $_GET['b'];

if($a != $b && md5($a) == md5($b)){
    // wow, glzjin wants a girl friend.
-->
```



5. 传入两个array绕过

因为`md5(array(1)) == Null`，`md5(array(2)) == Null`

![image-20211011132602010](https://i.loli.net/2021/10/11/NroFIMx3gazUtW8.png)



6. 继续访问跳转地址

![image-20211011132854717](https://i.loli.net/2021/10/11/48M1rYoRVXQEJbn.png)

```php
 <?php
error_reporting(0);
include "flag.php";

highlight_file(__FILE__);

if($_POST['param1']!==$_POST['param2']&&md5($_POST['param1'])===md5($_POST['param2'])){
    echo $flag;
}
```



7. 和上一步差不多的方法，改为POST

![image-20211011133447923](https://i.loli.net/2021/10/11/VvzCQwJjgdZclb7.png)



Get Flag!

