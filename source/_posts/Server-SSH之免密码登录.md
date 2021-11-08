---
title: SSH之免密码登录
comments: false
categories:
  - - 服务器
  - - 协议类
tags:
  - SSH
  - 协议类
top: false
desc: SSH基础学习之免密码登录服务器
keywords: 'SSH, 快捷, 配置, config, 协议类, 服务器, 免密码'
abbrlink: 1431
date: 2019-09-03 21:34:27
updated: 2019-09-03 21:34:27
---

#### 背景

{% note warning %}
前几天的文章中介绍了SSH的快捷配置，今天讲述一下SSH免密码登录服务器，这个操作在玩服务器中经常用到，建议收藏。
{% endnote %}

{% label default@SSH %} {% label success@免密码 %} {% label info@SSH配置 %}


<!--more-->
<hr />

#### 正文

> 生成密钥公钥

```
ssh-keygen -t rsa -P '' -f ~/.ssh/id_dsa
```
这个命令会产生一个公钥文件id_rsa.pub和密钥文件id_rsa，
* -t rsa：表示使用密钥的加密类型
* -P ''：表示不需要密码登录
* -f ~/.ssh/id_dsa：表示密钥存放的路径为用户/.ssh/id_dsa

> 公钥上传服务器

```
ssh-copy-id 用户@服务器IP
输入用户登录密码
```
执行这个命令，会把刚生成公钥文件内容复制到服务器~/.ssh/authorized_keys文件中。
也可以用其他方式，只要把公钥复制到服务器authorized_keys文件中即可。

这样就实现SSH免密码登录服务器，加上上篇SSH配置中config，以后直接ssh XXXX即可登录服务器。

#### 特别说明

服务器ssh目录以及authorized_keys文件的权限：

- chmod 700 ~/.ssh/
- chmod 600 authorized_keys
