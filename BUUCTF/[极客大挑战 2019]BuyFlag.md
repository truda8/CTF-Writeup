# [极客大挑战 2019]BuyFlag

1. 菜单打开*/pay.php*，发现重要提示信息

```
Flag need your 100000000 money

If you want to buy the FLAG:
	You must be a student from CUIT!!!
	You must be answer the correct password!!!
```



2. 查看源代码发现注释的PHP代码段

```php
// ~~~post money and password~~~
if (isset($_POST['password'])) {
	$password = $_POST['password'];
	if (is_numeric($password)) {
		echo "password can't be number</br>";
	}elseif ($password == 404) {
		echo "Password Right!</br>";
	}
}
```



3. 发现存在cookie

   把cookie的user值改为1就表示是CUIT的学生

```
Cookie: user=1
```



4. 使用php弱类型判断`password=404e`绕过密码检测



5. 使用科学计数法`money=10000e39`绕过金额长度限制

![image-20211008155821845](https://i.loli.net/2021/10/08/AcYJeUxh2oyFkpE.png)
