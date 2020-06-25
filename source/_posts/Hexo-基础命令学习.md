---
title: Hexo基础命令学习
comments: false
desc: 关于Hexo基础命令学习记录
categories:
  - [Hexo]
tags: [Hexo]
keywords: hexo, next, Hexo, 博客, blog, 基础命令
abbrlink: 39009
date: 2018-10-23 23:11:48
updated: 2018-10-23 23:11:48
---

#### 简介
{% note success %}
昨天写了blog的初始化搭建(hexo + next)，乘胜追击，学习查看了一些hexo基础的命令，总结一下分享。
{% endnote %}

<!--more-->
<hr />

基于官方的手册，很基础，加了一些自己的见解。

![hexo_help](hexo_help.png)


#### 预览

| id  |   name   |     brief      | frequency |
|:---:|:--------:|:--------------:|:---------:|
|  1  |   init   |     初始化     |    🌟     |
|  2  |   new    |    新建文章    |  🌟🌟🌟   |
|  3  | generate |  生产静态文件  |  🌟🌟🌟   |
|  4  | publish  |    草稿发布    |    🌟     |
|  5  |  server  |    启动服务    |   🌟🌟    |
|  6  |  deploy  |    部署网站    |   🌟🌟    |
|  7  |  rende   |    渲染文件    |    🌟     |
|  8  |  clean   |    清除缓存    |    🌟     |
|  9  |   list   |  列出网站资料  |    🌟     |
| 10  | version  | 显示 Hexo 版本 |    🌟     |
| 11  | --debug  |   debug模式    |  🌟🌟🌟   |

#### 正文

> init
```
$ hexo init [folder]
```
新建一个网站。folder文件夹已存在，会重新建里一个新的blog，主要用户初始化。

> new

```
$ hexo new [layout] <title>
```
新建一篇文章。如果没有设置 layout 的话，默认使用 _config.yml 中的 default_layout 参数代替。**如果标题包含空格的话，请使用引号括起来。**
一般情况有3种，page、post、draft

> generate

```
$ hexo generate
$ hexo g
```
生成静态文件，用于打包，第二行是简写。
选项	描述
-d, --deploy	文件生成后立即部署网站
-w, --watch	监视文件变动

> publish

```
$ hexo publish [layout] <filename>
$ hexo publish draft 常用语
```
发表草稿，就是通过hexo new draft建立的文章。

> server

```
$ hexo server
$ hexo s
```
启动服务器。默认情况下，访问网址为： http://127.0.0.1:4000/。
选项	描述
-p, --port	重设端口
-s, --static	只使用静态文件
-l, --log	启动日记记录，使用覆盖记录格式

> deploy

```
$ hexo deploy
$ hexo d
```
部署网站，第二行简写。

参数	描述
-g, --generate	部署之前预先生成静态文件

> render

```
$ hexo render <file1> [file2] ...
```
渲染文件。

参数	描述
-o, --output	设置输出路径

> migrate

```
$ hexo migrate <type>
```
从其他博客系统 迁移内容，***还没用过***。

> clean

```
$ hexo clean
```
清除缓存文件 (db.json) 和已生成的静态文件 (public)。
在某些情况（尤其是更换主题后），如果发现您对站点的更改无论如何也不生效，您可能需要运行该命令。

> list

```
$ hexo list <type>
```
列出网站资料，types：page，post，route，tag，category。
![hexo_list](hexo_list.png)

> version

```
$ hexo version
```
显示 Hexo 版本。
![hexo_version](hexo_version.png)

> 选项

- 安全模式
```
$ hexo --safe
```
在安全模式下，不会载入插件和脚本。当您在安装新插件遭遇问题时，可以尝试以安全模式重新执行。

- 调试模式
```
$ hexo --debug
```
在终端中显示调试信息并记录到 debug.log。当您碰到问题时，可以尝试用调试模式重新执行一次，并提交调试信息到 GitHub。

- 简洁模式
```
$ hexo --silent
```
隐藏终端信息。

- 自定义配置文件的路径
```
$ hexo --config custom.yml
```
自定义配置文件的路径，执行后将不再使用 _config.yml。

- 显示草稿
```
$ hexo --draft
```
显示 source/_drafts 文件夹中的草稿文章。

- 自定义 CWD
```
$ hexo --cwd /path/to/cwd
```
自定义当前工作目录（Current working directory）的路径。

#### 个人建议

- 命令一
```
hexo server -p 8888 --debug --draft
```
以-p参数指定服务的端口启动，加上--debug模式，便与调试
--draft 可以把草稿的文章也加载显示

- 命令二
```
hexo g -d
```
重新生产静态文件并上传github.io，刷新github的网站。

#### 参考

[hexo官网](https://hexo.io/zh-cn/docs/commands.html)
