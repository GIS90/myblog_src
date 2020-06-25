---
title: Linux学习之基础篇-tar
comments: false
categories:
  - [Linux]
tags: [Linux, Linux基础篇]
top: false
abbrlink: 29844
date: 2017-06-04 17:30:42
updated: 2017-06-04 17:30:42
desc: 记录Linux命令学习基础篇之tar，用于打包文件、目录等文件
keywords: linux, tar, 解压, 压缩, 打包, 服务器, 命令, shell, bash
---

![](/images/article_linux_tar.png)

{% cq %}
<font size=6.5 color='red'>tape archive</font>
{% endcq %}

<!--more-->
<hr />

### 简介
{% note warning %}
学习tar的用法【tar 参数 文件名 文件目录】
{% endnote %}

### 介绍

今天学习的命令跟文件打包、压缩、解压相关，而且特别提醒一下打包与解压缩不是一码事。打个比方，打包就把一堆文件、文件夹等放在一块；压缩就是把文件进行换种格式进行存储，目的是为了减小size。
在linux系统下，常用的一个命令***tar***，包含了以上的所有功能，在日常维护中非常常用，功能十分强大。当然，你也可以使用gzip、bzip等解压缩命令，但是一个***tar***就可以搞定所有事，何乐而不为。
tar打包后的文件通常以**.tar**进行结尾，压缩而是相对于文件格式而定，通常有**.bz、.gz、.Z**等等。

### 推荐指数
```
🌟🌟🌟🌟🌟
```

### 正文

这个命令用的频率很大，可以打包、压缩单文件、多个文件、多目录、文件+目录，建议记住常用参数，如果记不住，那么就多敲命令，熟能生巧。

#### 格式

【tar 参数 文件名 文件目录】

#### 参数说明
这个命令的参数相对来说还是比较多的，我这里列举了常用的参数，如果有兴趣查看全部参数的同学请**man tar**或者自行百度。

> -c

创建一个新的压缩文件。

> -x

解压文件，文件是压缩格式，与**-c**相反。

> -t

显示压缩文件的内容，对于只想查看却不想解压使用这个即可，常用。

> -z

解压**gzip**格式的文件。

> -j

解压**bzip2**格式的文件。

> -Z

解压**.Z**格式的文件。

> -p

保持原文件的原来属性（属性不会依据使用者而变）

> -v

显示打包、压缩、解压文件的详细过程。

> -f

指定压缩文件，通常会写上文件名，**-f**可省略。

> --exclude FILE

在压缩的过程中，排除指定的文件不进行打包、压缩

#### 常用命令

> 解包 && 打包

```
tar xvf file_name.tar
tar cvf file_name.tar file1 file2 dir1 dir2 ...
```

> .tar.gz格式

解压：
```
tar zxvf file_name.tar.gz
```
压缩：
```
tar zcvf file_name.tar.gz file1 file2 dir1 dir2 ...
```

> .tar.bz格式

解压：
```
tar jxvf file_name.tar.bz
```
压缩：
```
tar jcvf file_name.tar.bz file1 file2 dir1 dir2 ...
```

> .tar.Z格式

解压：
```
tar Zxvf file_name.tar.Z
```
压缩：
```
tar Zcvf file_name.tar.Z file1 file2 dir1 dir2 ...
```

> 查看打包、压缩文件

主要用了**-t**参数，面对不同的压缩文件，更改对应参数：
```
tar -ztvf file.tar.gz
```

> 排除部分文件

压缩指定文件夹file下的文件，但是排除file目录的子文件sub_file。
```
tar -zcvf file.tar.gz file/* --exclude file/sub_file
```

### 说明

```
tar -cvf file.tar file1 file2 ...
tar -zcvf file.tar.gz file1 file2 ...
tar -zxvf file.tar.gz
```
第一条：打包文件 && 不压缩
第二条：打包 && gzip格式压缩
第三条：gzip格式解压

{% note info%}
- 压缩-c（compress）
- 解压-x
- 查看-t
- 压缩/解压格式：z-zip（常用）、j-bz、.Z-.Z
{% endnote %}

### 补充

**.rar、.zip**格式的日常经常遇到，这里简单说明一下怎么处理

> .zip

主要用**zip && unzip**命令。
解压：
```
unzip file_name.zip
```
压缩：
```
zip file_name.zip file1 file2 dir1 dir2 ...
```

> .rar

主要用**rar**命令。
解压：
```
rar x file_name.rar
```
压缩：
```
rar a file_name.rar file1 file2 dir1 dir2 ...
```

### 学习



### 多说一句

涉及到文件权限等文件，记得一定要加**-p**参数，tar打包、压缩文件进行传输，不会影响文件的用户、用户组、权限等信息，之前直接传输文件，导致用户、权限都发生改变了，趟过坑，不了解的同学注意一下。
