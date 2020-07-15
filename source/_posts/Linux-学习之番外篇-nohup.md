---
title: Linux学习之番外篇-nohup
comments: false
categories:
  - [Linux]
tags: [Linux, Linux番外篇]
top: false
abbrlink: 23692
date: 2020-05-13 09:46:47
updated: 2020-05-13 09:46:47
desc: 总结一下nohub命令在Linux的相关操作
keywords: Linux, nohub, &
---

![](/images/article_linux_nohup.jpeg)

#### 简介
{% note danger %}
<font color="#red" size="5">用途</font>：不挂断地运行命令。
<font color="#blue" size="5">语法</font>：nohup Command [ Arg … ] [　& ]
<font color="#white" size="5">描述</font>：nohup 命令运行由 Command 参数和任何相关的 Arg 参数指定的命令，忽略所有挂断（SIGHUP）信号。在注销后使用 nohup 命令运行后台中的程序。要运行后台中的 nohup 命令，添加 & （ 表示”and”的符号）到命令的尾部。
{% endnote %}

<!--more-->
<hr />

在Linux系统中，多账户进行ssh登录是常有的事，但是有时候会去查看一下登录的用户都有谁以及相关的登录信息。

#### 总结

|  命令  |                         说明                         |
|:------:|:----------------------------------------------------:|
|   w    |               显示当前登录的用户及信息               |
|  who   | 显示当前已经登录的用户名、终端名称、登录时间及登录IP |
| whoami |                 显示当前用户的用户名                 |
|   id   |               用于check系统是有此用户                |
|  last  |             显示近期用户或终端的登录情况             |

#### w

显示当前登录的用户及信息，除了这些还会显示当前登录了几个用户、系统当前的load。

```
[root@bash ~]# w
 20:22:25 up 15:55,  3 users,  load average: 0.00, 0.01, 0.05
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
root     tty1                      Tue21   15:27m  0.09s  0.09s -bash
root     pts/0    192.168.1.116    19:23    1.00s  0.12s  0.01s w
root     tty2                      07:43   19:29   0.02s  0.02s -bash
```

#### who

显示当前已经登录的用户名、终端名称、登录时间及登录IP。

```
[root@bash ~]# who
root     tty1         2019-12-24 21:23
root     pts/0        2019-12-24 19:23 (192.168.1.116)
root     tty2         2019-12-24 07:43
```
#### whoami

显示当前用户的用户名。
```
[root@bash ~]# whoami
root
```

{% raw %}
<div class="post_cus_note">额外赠送</div>
{% endraw %}

#### id

用于显示用户的ID，以及所属群组的ID，主要用于check系统是有此用户。
```
[root@bash ~]# id root
uid=0(root) gid=0(wheel) groups=0(wheel)
```

#### last

显示近期用户或终端的登录情况。
```
[root@bash ~]# last -n 5
root     pts/0        :0.0             Wed Apr 25 10:12   still logged in
root     pts/1        :0.0             Wed Apr 25 10:06 - 10:10  (00:03)
root     pts/0        :0.0             Wed Apr 25 10:06 - 10:10  (00:03)
root     pts/0        :0.0             Wed Apr 25 10:02 - 10:06  (00:04)
root     pts/0        :0.0             Wed Apr 25 09:51 - 09:51  (00:00)
