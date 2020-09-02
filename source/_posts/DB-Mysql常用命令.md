---
title: Mysql常用命令
comments: false
categories:
  - 数据库
tags:
  - Mysql
top: false
desc: Mysql数据库常用命令记录
keywords: 'Mysql, 数据库, 常用命令, select, create, user, table, database'
abbrlink: 14802
date: 2020-07-07 21:00:04
updated: 2020-07-07 21:00:04
---

![](/images/article_mysql.png)

{% label default@Mysql %} {% label primary@select into %} {% label success@create %} {% label info@user %}

{% note primary %}
记录一下常用的命令，虽然关于查询相关的命令常用（select、order by、where、join等），但是关于建立数据库、建立用户、授权等并不常用的命令，做个整理，也方便了自己进行查询和使用
{% endnote %}

<!--more-->
<hr />

> #### 创建数据库

```
create database 数据库名称 default character set utf8 collate utf8_general_ci;
```

> #### 创建用户

```
create user '用户名'@'%' IDENTIFIED BY '密码';
-- % 表示通配符，任意远程主机都可以连接主机【常用】

create user '用户名'@'localhost' IDENTIFIED BY '123456';
-- localhost 表示本机，用户只有通过本机进行连接主机

create user '用户名'@'XXX.XXX.XX.XXX' IDENTIFIED BY '123456';
-- XXX.XXX.XX.XXX 表示ip，用户只有通过指定的ip主机进行连接
```

> #### 授权

```
# 所有权限 所有表【常用】
grant all on *.* to '用户名称';

# 所有权限 指定数据库【常用】
grant all on 数据库名称.* to '用户名称';

# 指定权限 指定数据库
grant select,insert,update,delete,create on 数据库名称.* to '用户名称';

# 刷新生效
flush  privileges;

# 查看权限
show grants for '用户名称';
```

> #### 其他

数据库列表：show database;
表列表：show tables;
切换数据库：use 数据库;

{% raw %}
<div class="post_cus_note">查询方面略</div>
{% endraw %}
