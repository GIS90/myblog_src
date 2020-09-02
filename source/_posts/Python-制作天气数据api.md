---
title: Python制作天气数据api
desc: 利用Python语言开发一个天气数据api，有获取数据源的api
categories:
  - [Python]
tags: [Python, Python程序篇, 爬虫]
comments: false
keywords: python, api, 天气, 程序, 爬虫, 数据库, 脚本, 程序
abbrlink: 53966
date: 2018-09-24 11:55:30
---

{% label default@Python实战 %} {% label primary@天气API %} {% label success@爬虫系列 %} 

### 简介
    还再找免费的天气API接口吗，这里给你答案
    开发语言：python
    技术方案：requests + sqlalchemy
    感谢python，（数据源：官方中国天气网http://www.weather.com.cn）

<!--more-->
<hr />

### 正文
​​​偶然工作中用到了天气状况数据，后来就不需要了，但还是想做一个天气的，因为想给自己的女票做个天气短信提醒。说搞就搞，第一想法就是apistore，上去了之后，好贵。。。。。。<!-- more -->百度一了一下，全都不好用，决定自己写一个，自己动手丰衣足食嘛。再百度天气，中国天气网是第一条，还是官方的，说明应该不错，点进去之后，看了数据，需求基本满足了，那么，走起。
![百度搜索引擎（本人声明，不是百度员工）](baidu.jpg)
#### 查询数据源
google打开天气网，搜了下北京天气，alt+cmd+i打开调试模式（mac快快捷键），network查看数据来源。经过分析，基本可以确定数据主要来源于2个接口：http://d1.weather.com.cn/dingzhi/101010100.html?_=1537709265753 （地之一）和http://d1.weather.com.cn/sk_2d/101010100.html?_=1537709265752 （地址二），多打开了几个别的城市进行查看，最后结论：101010100参数一城市的id值，1537709265753参数二时间戳（毫秒级）。
![调试&&分析调试&&分析](tiaoshi.jpg)

#### 获取城市id
    在官网反反复复尝试获取城市的数据，发个城市id有几个规律：
* 城市id由9位数字组成(可能大家觉得感觉有点废话了，别急往后看)，例如：北京101010100。
* 城市id的第三位，第四位是表示省份（免费普及一下：中国34个省级行政区域，包括23个省，5个自治区，4个直辖市，2个特别行政区），01-北京，02-上海，03-天津，04-重庆。。。34-台湾。
* 后三位尾数，针对于直辖市，尾数从000开始计数，非直辖市尾数从001开始计数。
* 天气网数据细到乡镇，街道。乡镇的id：101080503(cityid) + xxx(数字，001开始)，12位组成；街道数据过于细致，没必要获取，而且本人能力有限，只初始化了到城市级别的的数据。
* 额外赠送：中国每个省份的城市最大值位21，代码中会用到。

知道规律，也了解了request url，response，就可以搞定城市id的数据源了。解决方法如下：
* 语言：python
* 思想：依据id的范围生成范围id，requests去get请求，获取结果
* 要点：省份的标志位01～04位直辖市，05～34非直辖市，城市的标志位01～23即可；header必须含有Referer值，应该用来做一个访问标识response返回值类型是string，但是weatherinfo的信息为json，需转化。不多说，直接上代码：
![城市id值生成城市id值生成](id.jpg)

#### 数据入库
数据库决定直接用sqlite，主要考虑到数据库的可移植性，git项目直接运行就可以，不用额外配置数据库，而且单张表，数据量不会很大，性能没有太高要求。python + requests + sqlalchemy + db，玩py的不知道sqlalchemy&&requests，自己赶快恶补一下吧。。。废话也不多说，git项目看db.py文件，创建表以及数据库见下图：
![数据库创建&&表查询数据库创建&&表查询](db.jpg)
城市id获取的整理流程设计ok，执行python citys.py就可以见证奇迹。不过，这个奇迹有点慢而已，我的本大概执行了30个小时左右，后来想的是python配合多进程（GIL机制，不要使用多线程）来提速，搞了个pool在那，不过我把多进程注释了，有兴趣的人可以去试下多进程。

#### api接口服务
做web服务，flask是不错的选择，简单易用，性能也不差。用blueprint做了个weather的接口，但是信息由地址一与地址二组成，地址一主要用来获取最高/最低温度，地址二获取实时的天气相关信息，请求的地址参数均由第三步回去的城市id以及时间戳。

requests基础：http://docs.python-requests.org/zh_CN/latest/user/quickstart.html

请求的时候，我把浏览器正常访问的header都记录，请求成功，把结果封装json返回。在controller那，我对请求方式，请求参数做了限制，加强接口的严谨性。详细自己看代码，post请求的参数那块，args，form，json，get_json分不清的，请自行百度，我做了个小技巧：
![获取post请求参数获取post请求参数](api.jpg)

#### 测试
这里介绍2种测试方式，postman + curl。

curl：curl -X POST http://127.0.0.1:8888/weather/ -H 'Content-Type: application/json' -d '{"city": "昌平"}' | python -m json.tool

postman：图形化界面。。。自己点把

没有curl命令的，自己搞下，做开发的话，不知道curl，会很low的，看下结果，完美：
![成果](test.jpg)



### 总结
代码很简单，不过在获取数据源id上花费了一些时间，后来一想，城市id的表有个问题，表有：id，cityname，cityid 3个字段，没有记录省份，查询同名的城市可能会有问题，后续在改吧。。。就先到这里了，我是程序猿，python程序猿。

二期功能：定时任务 + 短信提醒 + 邮件报警

项目git地址：https://github.com/GIS90/weathers
