# git commit -m "whatever"

1. 打开页面，得到一段加密的字符串和提示：

```
+M/pqMuo4pevO4qE7ETogLZjXSoiLhuqpmWh21pKXOpjftRMSq+ltAaloVOlwR3cGkaBeYxLQEb2kJ7FZg4UBxawjJvpcyKebpVoz6no
Only if you could see the source code.
```



2. 尝试扫描路径，发现存在**/.git/**路径

利用.git源代码泄露利用工具 [GitHack](https://github.com/lijiejie/GitHack) ，得到网站源代码

```
├── Crypt
│   ├── AES.php
│   ├── Base.php
│   ├── Blowfish.php
│   ├── DES.php
│   ├── Hash.php
│   ├── RC2.php
│   ├── RC4.php
│   ├── RSA.php
│   ├── Random.php
│   ├── Rijndael.php
│   ├── TripleDES.php
│   └── Twofish.php
├── File
│   ├── ANSI.php
│   ├── ASN1.php
│   └── X509.php
├── Math
│   └── BigInteger.php
├── Net
│   ├── SCP.php
│   ├── SFTP
│   │   └── Stream.php
│   ├── SFTP.php
│   ├── SSH1.php
│   └── SSH2.php
├── System
│   ├── SSH
│   │   └── Agent.php
│   └── SSH_Agent.php
├── bootstrap.php
├── index.php
├── openssl.cnf
└── tempCodeRunnerFile.py
```



3. 审计代码，发现**index.php**里有个**crypto**类，存在两个方法`encryp()`和`decrypt()`，即加密和解密的方法



4. 解密过程

![image-20211009153345514](https://i.loli.net/2021/10/09/kBeQPfOmI7DnRFW.png)



5. 调用`decrypt()`方法解密

```php
$privatekey = "mRHpcEckKATdwDC/CwpRinDTiAYrn9lzWpTo277omKs=";
$encrypted = "rI6D6aK8m1HhT1oSfsP87trNCrLMMc0MoySGaVbku4H9A3WqS1CgEbhAdZ3VWMAoFuPr9WfG2s5szKfgUFnKnzqv7CieKQvyK/tplDZp ";
$dnc = crypto::decrypt($encrypted, $privatekey);
echo $dnc;
```



6. 采坑

这里有个坑，解密代码中调用了`sodium_crypto_secretbox_open()`这个方法，而这个方法只有 (PHP 7 >= 7.2.0, PHP 8) 的版本才有，使用其它PHP版本运行会报错

![image-20211009153723628](https://i.loli.net/2021/10/09/wJnQPI1Gl74YfHC.png)



7. 运行解密代码，get flag！

![image-20211009154036362](https://i.loli.net/2021/10/09/6AZHgv4MYo1sDQj.png)

