---
title: Linux-学习之基础篇-cat
comments: false
categories:
  - [Linux]
tags: [Linux, Linux基础篇]
top: false
abbrlink: 10790
date: 2020-08-03 15:16:08
updated: 2020-08-03 15:16:08
desc: 记录Linux命令学习基础篇之cat，用于查看文件
keywords: linux, cat, 服务器, 命令, shell, bash
---

![](/images/article_linux_cat.jpeg)

{% label danger@Linux %} {% label primary@cat %} {% label success@基础教程系列 %}

{% cq %}
<font size=6.5 color='red'>concatenate files and print on the standard output</font>
{% endcq %}

<!--more-->
<hr />

### 简介

{% note default %}
你看没错，本篇研究的是**cat**，不顾不是会动的cat，它是用来查看日志的cat。
{% endnote %}

### 介绍

cat主要使用来查看文件的命令，其他的命令还有tac、tail（tail -f xxx 动态的查看日志）、awk（增强篇中已有）、sed、less、more等等，很多命令。

cat主要用来<font size=6.5 color='red'>**全量查看日志**</font>。

### 正文

#### 格式

```
cat [参数] [文件名]
```

#### 参数说明

> -n

对输出的文件添加**行号**，包含空行。

> -b

对输出的文件添加**行号**，去掉空行。


#### 常用命令

> 基本

```
cat 文件名
```
可以是相对路径，也可以是绝对路径。

> 输出行号

```
cat -n 文件名

cat -n 文件名 > 新文件
```
第二个命令可以把原来不带行号的文件输出到新的文件，并且带行号。

> 查找关键字的行

```
cat 文件名 | grep "关键字"
```
这个命令平时用的相对较多。

### 补充

关于其他查看日志的方式以后会陆续给出文章。
