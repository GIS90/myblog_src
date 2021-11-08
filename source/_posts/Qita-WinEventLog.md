---
title: Win Server服务器EventLog中的6005、6006、6008、6009、6013
comments: false
categories:
  - - Windows
tags:
  - Windows
top: false
desc: 关于Windows Server R2中的6005、6006、6009、6013
keywords: 'Windows, Server, EventLog, 6005, 6006, 6008, 6009, 6013'
abbrlink: 54459
date: 2021-05-21 09:05:20
updated: 2021-05-21 09:05:20
---

#### 背景

{% note primary %}
早上访问web项目，发现挂掉了，以为是内网网线的问题（本人电脑内外网跳板机），主要有线转换头经常出现问题，但是整了半天依然不行，于是打开服务器一看，什么东西都没了，一看就是重启了，于是需要查找到什么时候重启的，学会了查看系统的EventLog，记录一下用到的6005, 6006, 6008, 6009, 6013。
{% endnote %}

{% label info@Windows %} {% label primary@EventLog %}

<!--more-->
<hr />

#### 功能查询

查看系统的日志记录，查询服务器发生了哪些明细，所在位置：
<font size=5.5 color='blue'>我的电脑 > 管理 > 服务管理器  >  诊断 >  事件查看器 > windows日期 > 系统</font>

![](eventlog.png)

主要功能说明：
- 目录：EventLog所在的功能树
- 事件日志：服务器的事件日志历史记录
- 事件明细：对于历史记录的详细说明
- 功能区：对EventLog的常用功能，主要用到筛选当前日志

点击上面的历史事件，可以在明细区域查看具体情况。

#### 筛选功能

利用筛选功能选出需要的日志，主要有3大筛选条件：
- 记录时间：可以选取近1h、12h、24h、7天、30天
- 事件来源：选取eventlog、Eventlog
- 事件ID：输入需要过滤的事件ID

![](query.png)

#### EventLog ID

|  ID   | level ｜ describe |                                                                                                 |
|:-----:|:-----------------:|:--------------------------------------------------------------------- |
| 6005  |       信息        | 事件服务日期启动（开机）                                                                        |
| 6006  |       信息        | 事件服务日期关闭（关机）                                                                        |
| 6008  |       错误        | 上一次系统的 4:12:37 在 ?2021/?5/?21 上的关闭是意外的（记录系统意外关机事件）                   |
| 6009  |       信息        | Microsoft (R) Windows (R) 6.01. 7601 Service Pack 1 Multiprocessor Free（服务器开机的一些信息） |
| 60013 |       信息        | 记录操作系统运行了多久时间，24h运行一次                                                         |

破案了，原来是断电了，服务器来电后自己又自己起来了，但是服务全没了。

<font size=6.5 color='red'>记录遇到的各种Eventlog ID，持续更新中。。。。。。</font>
