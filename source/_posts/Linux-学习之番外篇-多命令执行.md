---
title: Linux学习之番外篇-多命令执行
comments: false
categories:
  - [Linux]
tags: [Linux, Linux番外篇]
top: false
abbrlink: 64874
date: 2019-06-26 20:26:09
updated: 2019-06-26 20:26:09
desc: Linux学习之番外篇-多命令执行
keywords: Linux, 多命令执行, &, &&, ||, shell
---

#### 简介
{% note danger %}
解决多命令command1，command1，command1...。
{% endnote %}

<!--more-->
<hr />

学习以下多命令一起执行：&、&&、；、||。

#### 推荐指数
🌟🌟🌟🌟🌟

#### 使用方法

> ;

语法：command1 ; command2 \[; command3\] ...
不管前面命令执行成功没有，后面的命令按顺序继续执行。

> &

语法：command1 & command2 \[& command3\] ...
多命令同时执行，互不影响。
```
ls & ll & ls
```

> &&

语法：command1 && command2 \[&& command3\] ...
命令之间使用 && 连接，实现逻辑<font color="red" size=5>与</font>的功能，只有左边的命令执行成功，后面命令才继续执行。
```
touch 1.txt && rm ~/Desktop/1.txt && echo "rm success"
```
先touch一个1.txt文件，接下来在rm删除，最后输出success。


> ||

语法：command1 || command2 \[|| command3\] ...
命令之间使用 || 连接，实现逻辑<font color="red" size=5>或</font>的功能，只有左边的命令执行失败，后面命令才继续执行。
```
las || echo "无命令"
```
