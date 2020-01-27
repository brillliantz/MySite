---
title: 用企业微信API开发微信机器人
date: 2017-02-26
draft: false
tags:
- WeChat
- Python
---

记录了Python学习的历程和用爬虫解决实际问题的经历.

<!--more-->


### 相关链接
- [企业号管理官网](https://qy.weixin.qq.com/)
- [企业号开发API](http://qydev.weixin.qq.com/wiki/index.php)
- [企业号API官方测试工具](http://qydev.weixin.qq.com/debug)

### 流程
1. 官网创建管理组，创建好后即得到`corpID`和`corpSecret`
2. 通过主动调用接口获取`access_token`，注意有过期时间
3. 通过消息发送接口发送消息，`access_token`放在URL里，发送的数据类型、数据内容等放在POST命令的`data`里


### 注意易错
主动调用发送消息，post的data不能是python的dictionary，而是需要对dict进行*JSON格式化*，可使用`json.dumps()`


### 简单示例
```python
import requests
import time
import ast
import json

class Wechat(object):
    def __init__(self, corp_id_, corp_secret_):
        self.url_prefix = r'https://qyapi.weixin.qq.com/'
        # token may expire, so we should record the time we get it.
        self.token_time = None
        self.corp_id = corp_id_
        self.corp_secret = corp_secret_
        #self.s = requests.Seesion()
        self.msg_header = {"Content-Type": "application/json; charset=utf-8"
                          }

    def get_token(self):
        url = self.url_prefix + r'cgi-bin/gettoken'
        params_ = {'corpid': self.corp_id,
                   'corpsecret': self.corp_secret
                  }
        res = requests.get(url, params=params_)
        self.token_dict = ast.literal_eval(res.content)
        self.token_dict['init_time'] = time.localtime()

    def json_encode(self, s):
        return json.dumps(s)

    def send_msg(self, content, userid_list=None, 
                 partyid_list=None, tag_list=None):
        if userid_list:
            touser = '|'.join(userid_list)
        else:
            touser = '@all'
        if partyid_list:
            toparty = '|'.join(partyid_list)
        else:
            toparty = ''
        if tag_list:
            totag = '|'.join(tag_list)
        else:
            totag = ''
        
        data_ = {
                "touser": touser,
                "toparty": toparty,
                "totag": totag,
                "msgtype": "text",
                "agentid": 1,
                "text": {
                         "content": content
                        },
                "safe":0
               }

        data_ = self.json_encode(data_)
        url = (self.url_prefix
               + r'cgi-bin/message/send?access_token='
               + self.token_dict['access_token']
              )
        res = requests.post(url, data=data_)
        return res
```
