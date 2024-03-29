---
title: Python模块之dtalk钉钉消息
comments: false
categories:
  - [Python]
tags: [Python, Python模块系列]
top: false
abbrlink: 58292
date: 2022-09-05 20:59:18
updated: 2022-09-05 20:59:18
desc: Python模块之dtalk钉钉消息
keywords: Python模块之config配置解析
---


![](/images/article_python_module.jpeg)

{% label primary@Python %} {% label info@Python模块系列 %}

{% raw %}
<div class="post_cus_note">Python模块系列</div>
{% endraw %}

<!--more-->
<hr />


Python项目常用的模块代码。


#### 版本

|  名称  | 版本 |
|:------:|:----:|
| Python |  3   |


#### 描述

DingApi类，主要用请求dingTalk openApi来操作DingDing进行发消息等操作。
目前，只支持机器人推送消息操作
类添加了is_avail对access token进行判断是否可用，如果不可用中止程序


#### 设计

- 官网发消息API：https://developers.dingtalk.com/document/robots/chatbots-send-one-on-one-chat-messages-in-batches/h2-xsq-kwt-wyg
- Status JSON说明：http://pygo2.top/articles/40461/

#### 使用

```
json_message = {
    "title": "2021-12绩效明细",
    "text": "#### 2021-11绩效明细  \n  - 个人存款绩效：278  \n  - 贷款绩效：278  \n  - 部门履职绩效：278  \n  - 存款下降扣发：278  \n  - ![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png)"
}
user = 'manager2730'
dapi = DingApi()
res = dapi.robot2send(message=json_message, to_id=user)
print(res)
```

#### 源码

```
# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe:
    DingTalk Api class, it use to push message
    采用单例模式的DingApi类，主要用请求dingTalk openApi来操作DingDing进行发消息等操作。
    目前，只支持机器人推送消息操作
    类添加了is_avail对access token进行判断是否可用，如果不可用中止程序

base_info:
    __author__ = "PyGo"
    __time__ = "2021/11/23"
    __version__ = "v.1.0.0"
    __mail__ = "gaoming971366@163.com"
    __project__ = "open2lisapi"

usage:
    json_message = {
        "title": "2021-12绩效明细",
        "text": "#### 2021-11绩效明细  \n  - 个人存款绩效：278  \n  - 贷款绩效：278  \n  - 部门履职绩效：278  \n  - 存款下降扣发：278  \n  - ![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png)"
    }
    user = 'manager2730'
    dapi = DingApi()
    res = dapi.robot2send(message=json_message, to_id=user)
    print(res)

design:
    DingDing官网开放平台

reference urls:
    官网发消息API：https://developers.dingtalk.com/document/robots/chatbots-send-one-on-one-chat-messages-in-batches/h2-xsq-kwt-wyg
    Status JSON说明：http://pygo2.top/articles/40461/

python version:
    python3


Enjoy the good life everyday！！!
Life is short, I use python.

------------------------------------------------
"""
import sys
import json
import requests

from deploy.utils.base_class import Singleton
from deploy.utils.status import Status
from deploy.config import DTALK_TOKEN_URL, DTALK_BASE_URL, DEBUG
from deploy.utils.logger import logger as LOG

from alibabacloud_dingtalk.robot_1_0.client import Client as dingtalkrobot_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.robot_1_0 import models as dingtalkrobot__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class DtalkLib(object):
    """
    dingTalk Api class
    """
    def __init__(self, app_key, app_secret):
        if DEBUG:
            LOG.debug("DingApi class start initialize.")
        self.RC = 0
        self.app_key = app_key
        self.app_secret = app_secret
        self.base_api_url = DTALK_BASE_URL
        self.token_api_url = DTALK_TOKEN_URL
        self.msg_type = 'sampleMarkdown'
        self.access_token = self.get_token()
        self.client = self.create_client()

    def is_avail(self):
        """
        是否有access token，如果没有token，则中止发信息请求
        建议用sys.exit()优雅的方式退出
        """
        return True if self.access_token else False

    def close(self):
        """
        关闭实例，清除access token
        """
        self.access_token = ''

    def get_token(self) -> str:
        """
        获取唯一access token，2h有效期
        this function is static method, it use to get access token code from dingTalk open api
        :return: access token
        result type is string
        """
        if DEBUG:
            LOG.debug("DingApi get access token.")
        headers = {
            'Access-Control-Allow-Origin': '*'
        }
        params = {"appkey": self.app_key, "appsecret": self.app_secret}
        url = "%s%s" % (self.base_api_url, self.token_api_url)
        try:
            response = requests.get(url=url, headers=headers, params=params)
            if response.status_code == 200:
                json_res = response.json()
                if json_res and json_res.get("errcode") == 0:
                    return json_res.get("access_token")
        except Exception as e:
            LOG.error('Initialize dingTalk openApi access token occur error: %s' % e)
            return ''
        LOG.error('Initialize dingTalk openApi get access token failure, please try again later.')
        return ''

    @staticmethod
    def create_client() -> dingtalkrobot_1_0Client:
        """
        初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkrobot_1_0Client(config)

    def robot2send(self, message: json, to_id: str) -> json:
        """
        use dingtalk openApi to send message
        :param message: DingDing消息体，为MarkDown语法
        :param to_id: 接收人ID
        :return: json type result
            status_id: 状态码,
            status: success or failure,
            msg: 消息体
            data: 数据体（diact类型）
            具体说明：http://pygo2.top/articles/40461/
        """
        # check access token && parameters
        if not self.access_token:
            return Status(
                202, "failure", "Not found access token.", {}).status_body
        batch_send_otoheaders = dingtalkrobot__1__0_models.BatchSendOTOHeaders()
        batch_send_otoheaders.x_acs_dingtalk_access_token = self.access_token
        batch_send_otorequest = dingtalkrobot__1__0_models.BatchSendOTORequest(
            robot_code=self.app_key,
            user_ids=[to_id],
            msg_key=self.msg_type,
            msg_param=json.dumps(message)
        )
        try:
            response = self.client.batch_send_otowith_options(batch_send_otorequest, batch_send_otoheaders, util_models.RuntimeOptions())
            json_resp = {
                'process': response.body.process_query_key or '',
                'failure': response.body.invalid_staff_id_list or [],
                'control': response.body.flow_controlled_staff_id_list or []
            }
            return Status(
                100, "success", "成功", json_resp).status_body
        except Exception as e:
            msg = 'DingTalk send message to [%s] occur error: %s' % (to_id, e)
            LOG.error(msg)
            return Status(
                601, "failure", msg, {}).status_body
```

#### 系列


[Python模块之command系统命令](http://pygo2.top/articles/26110/)
[Python模块之excel模块](http://pygo2.top/articles/19275/)
[Python模块之logger日志](http://pygo2.top/articles/5145/)
[Python模块之utils公共方法](http://pygo2.top/articles/61799/)
[Python模块之watcher打点](http://pygo2.top/articles/31232/)
[Python模块之config配置解析](http://pygo2.top/articles/51787/)
[Python模块之dtalk钉钉消息](http://pygo2.top/articles/58292/)
[Python模块之企业微信](http://pygo2.top/articles/33254/)

更多模块请参考文章TAG进行查看。

<font size=6.5 color='red'>***Python模块系列，持续更新中。。。。。。***</font>
