---
title: 前端JavaScript全局对象获取通用方法
comments: false
categories:
  - [前端]
tags: [JavaScript]
top: false
abbrlink: 19661
date: 2023-04-08 22:07:23
updated: 2023-04-08 22:07:23
desc: 前端JavaScript全局对象获取通用方法
keywords: 前端JavaScript全局对象获取通用方法
---


![](/images/article_javascript.jpeg)

<!--more-->
<hr />

在学习ES6语法的过程中，看到了JavaScript获取全局对象的通用方法，记录上，以防日后用的上。

#### 方法一
```
(typeof window !== 'undefined'
   ? window
   : (typeof process === 'object' &&
      typeof require === 'function' &&
      typeof global === 'object')
     ? global
     : this);
```

#### 方法二
```
var getGlobal = function () {
  if (typeof self !== 'undefined') { return self; }
  if (typeof window !== 'undefined') { return window; }
  if (typeof global !== 'undefined') { return global; }
  throw new Error('unable to locate global object');
};
```

<font size=6.5 color='red'>坚持学习。。。。。。</font>
