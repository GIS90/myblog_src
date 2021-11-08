---
title: Brew安装与常用命令
comments: false
categories:
  - [MacOS]
tags: [MacOS, brew]
top: false
abbrlink: 12880
date: 2021-06-14 22:09:08
updated: 2021-06-14 22:09:08
desc: MacOS上的Brew命令的安装与基础使用
keywords: MacOS, brew, install, 包, 管理
---

![](/images/article_brew.png)

#### 问题背景

{% note primary %}
MacOS系统安装软件使用Brew进行管理，这里主要自己记录一下Brew不常用的命令，方便自己查找与使用。
{% endnote %}

<!--more-->
<hr />

#### 安装

item2直接执行。
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

等待执行结果，查看版本：
```
brew --version
```

brew安装软件目录：/usr/local/Cellar

#### 命令

> 搜索

```
brew search xxx
```

> 安装

```
brew install xxxx
```

> 卸载

```
brew uninstall xxxx
```

> 查询

```
brew info xxxx
```
主要查看具体的软件信息、下载地址、安装依赖、基础信息等等。

> 更新

```
brew update xxxx
```

> 查看安装列表

```
brew list
```

> 检测新版本

```
brew outdated xxxx
```

> 升级

```
# 升级所有 当然也可以指定升级
brew upgrade
# 升级指定软件
brew upgrade xxxx
```

> 打开官网

```
brew home
```

> 清理

```
brew cleanup
```

> 更多命令

```
man brew
```

#### 参考

官网：https://brew.sh/
