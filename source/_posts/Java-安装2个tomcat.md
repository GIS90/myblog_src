---
title: Windows安装2个Tomcat
comments: false
categories:
  - - Java
tags:
  - Java
  - Tomcat
top: false
desc: Windows安装2个Tomcat
keywords: 'Java, Tomcat'
abbrlink: 27869
date: 2023-01-13 15:35:46
updated: 2023-01-13 15:35:46
---

{% label primary@Java %} {% label success@Tomcat %}

#### 背景
{% note primary %}
在Windows上运行Tomcat6、Tomcat8，Tomcat与对应的Java有版本关系。
{% endnote %}

![](/images/article_youzan.jpeg)

<!--more-->
<hr />


#### 环境

| id  | Tomcat版本 | Java版本 |
|:---:|:----------:|:--------:|
|  1  |     6      |   1.6    |
|  2  |     8      |   1.8    |

#### 特殊说明

第一套Tomcat6与Java1.6正常配置，这里不做详细描述

#### 操作方式

安装JDK1.8与TOMCAT8，环境已经已存在tomcat6，如果只有一个tomcat不需要设置。
TOMCAT8/Bin/startup.bat、TOMCAT8/bin/setclasspath.bat最上面添加：
```
rem =====================================================================
rem tomcat
SET CATALINA_HOME=D:\apache-tomcat-8.5.59
SET CATALINA_BASE=D:\apache-tomcat-8.5.59
SET CATALINA_TMPDIR=D:\apache-tomcat-8.5.59\temp

rem java
SET JAVA_HOME=C:\Program Files\Java\jdk1.8.0_271
rem =====================================================================
```

<font color='red' size=4.5>坚持学习。。。。。。</font>！！！。
