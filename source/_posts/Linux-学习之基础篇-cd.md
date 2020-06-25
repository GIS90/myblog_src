---
title: Linux学习之基础篇-cd
comments: false
categories:
  - [Linux]
tags: [Linux, Linux基础篇]
top: false
abbrlink: 42764
date: 2017-05-24 17:31:20
updated: 2017-05-24 17:31:20
desc: 记录Linux命令学习基础篇之cd，用于变更目录change dir
keywords: linux, cd, 服务器, 命令, shell, bash
---

![](/images/article_linux_cd.png)

{% cq %}
<font size=6.5 color='red'>change dir</font>
{% endcq %}

<!--more-->
<hr />

### 简介

{% note warning %}
学习cd的用法【cd 目录】
{% endnote %}

### 介绍

前篇关于linxu的文章，介绍linux最常用的命令之一的**ls**，本篇介绍一下它的兄弟**cd**。这个命令用的太多了，我推测的全拼应该是**change dir**，没有查资料，如果错了，欢迎留言。

### 正文

#### 格式

```
cd [目录名]
```

#### 参数说明

没用过参数，下面学习中有个cd用法的介绍，有兴趣的可以看看。

#### 常用命令

> 基本

```
cd 目录
```
可以是相对路径，也可以是绝对路径

> 根目录

```
cd /
```
> 用户home目录

```
cd
cd ~
```
> 返回上级

```
cd ..
```
> 多个上级

```
cd ../../..
```

> 返回切换的上一个目录

```
cd -
```
这个命令平时用的相对较多。

### 补充

- "~"表示为用户home目录
- "."表示当前所在的目录
- ".."表示当前目录的上一层目录

### 学习

参数：https://www.computerhope.com/unix/ucd.htm
