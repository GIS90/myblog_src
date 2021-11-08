---
title: Linux-学习之增强篇-crontab
comments: false
categories: [Linux]
tags: [Linux, Linux增强篇]
top: false
abbrlink: 40314
date: 2020-04-01 10:11:01
updated: 2020-04-01 10:11:01
desc: 记录Linux命令学习基础篇之crontab
keywords: linux, crontab, 服务器, 命令, 定时任务, shell, bash
---

#### 简介
{% note danger %}
<font size=5.5 color='#FF6600'>Linux自带的定时任务命令</font>。
![](/images/article_crontab.png)
{% endnote %}

{% label danger@Linux %} {% label warning@crontab %} {% label success@高级教程系列 %} {% label info@定时任务 %}


<!--more-->
<hr />

#### 推荐指数
```
🌟🌟🌟
```

#### 基本介绍

定时去执行指定的程序。

首先，先查看一下命令基础使用规则：
```
[root@localhost ~]#cat /etc/crontab
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root

# For details see man 4 crontabs

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed
```
结合上图，可以语法糖：分钟 小时 日期 月份 星期 [用户] 命令

#### 参数详解

crontab的参数很少。

> -e

编辑任务，已vim的方式打开crontab的任务列表，可以进行新增、编辑、删除等任务操作。

> -l

查看任务，相当于cat 任务表。


#### 符号说明

> *

代表全部，默认*。

> /

代表除，符合能被后面等数整除的条件，例如：/2

> -

代表范围，8-12包含：8、9、10、11、12

> ,（英文）

代表指定的数，1,10,22，只有在1,10,22才执行


#### 常用命令


> 每小时的第5和第10分钟执行command

```
5,10 * * * * command
```

> 每隔5min执行command

```
*/5 * * * * command
```

> 每隔1小时执行command

```
* */1 * * * command
```

> 8点的第5分钟执行command：

```
5 8 * * * command
```

> 8-11点的第5和10分钟执行command：

```
5,10 8-11 * * * command
```

> 每周一8-11点的第5和10分钟执行command：

```
5,10 8-11 * * 1 command
```

> 每月1，5，10号的8-11点的第5和10分钟执行command：

```
5,10 8-11 1,5,10 * 1 command
```

#### 特别说明

crontab很简单，但是很实用，欢迎大家一起交流share。

<a href="/articles/44008/" target="_blank" class="block_project_a">Crontab指定用户运行任务</a>
