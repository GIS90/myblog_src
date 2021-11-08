---
title: MacOS配置svn免账号密码
comments: false
categories:
  - - 工具集
tags:
  - svn
top: false
desc: MacOS环境配置svn免密码
keywords: 'MacOS, svn, 免密码, checkout'
abbrlink: 49218
date: 2021-02-01 14:08:55
updated: 2021-02-01 14:08:55
---

![](/images/article_svn.jpg)

{% label primary@SVN %}


<!--more-->
<hr />

> 环境

MacOS Big Sur 11.1

> 版本

version 1.11.1 (r1850623)

> 配置

- 编辑配置文件

    vim ~/.subversion/config

    ```
    store-passwords = yes
    store-auth-creds = yes
    ```

- 权限配置

    ```
    sudo chmod 775 -R auth/
    ```
