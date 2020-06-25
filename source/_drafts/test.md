---
title: test
desc: est
categories:
  - 杂七杂八
tags:
  - 实验
abbrlink: 63534
date: 2019-05-15 20:22:27
updated: 2019-05-15 20:22:27
---

> cq

{% cq %}
一个爱老婆的Python程序猿。。。。。。
**PyGo²**
{% endcq %}

> button

{% btn https://www.baidu.com, 百度首页, download fa-lg fa-fw, 百度首页标题 %}

> video

{% video /publicfiles/xiao6.mp4 %}

<!--more-->

> exturl

{% exturl https://www.baidu.com 百度首页 %}

> fi-images

{% fi /images/article_wdyxxy.jpg %}
<img src="/images/article_wdyxxy.jpg" style="border:1.5px solid blue" alt=""/>

> note

{% note default %}
default 提示块标签
{% endnote %}

{% note primary %}
primary 提示块标签
{% endnote %}

> pdf

{% pdf /publicfiles/PythonStudy.pdf %}

> mermaid

{% mermaid graph TD %}
A[Christmas] -->|Get money| B(Go shopping)
B --> C{Let me thinksssss<br/>ssssssssssssssssssssss}
C -->|One| D[Laptop]
C -->|Two| E[iPhone]
C -->|Three| F[Car]
{% endmermaid %}



{% mermaid graph LR %}
47(SAM.CommonFA.FMESummary)-->48(SAM.CommonFA.CommonFAFinanceBudget)
37(SAM.CommonFA.BudgetSubserviceLineVolume)-->48(SAM.CommonFA.CommonFAFinanceBudget)
35(SAM.CommonFA.PopulationFME)-->47(SAM.CommonFA.FMESummary)
41(SAM.CommonFA.MetricCost)-->47(SAM.CommonFA.FMESummary)
44(SAM.CommonFA.MetricOutliers)-->47(SAM.CommonFA.FMESummary)
46(SAM.CommonFA.MetricOpportunity)-->47(SAM.CommonFA.FMESummary)
40(SAM.CommonFA.OPVisits)-->47(SAM.CommonFA.FMESummary)
38(SAM.CommonFA.CommonFAFinanceRefund)-->47(SAM.CommonFA.FMESummary)
43(SAM.CommonFA.CommonFAFinancePicuDays)-->47(SAM.CommonFA.FMESummary)
42(SAM.CommonFA.CommonFAFinanceNurseryDays)-->47(SAM.CommonFA.FMESummary)
45(SAM.CommonFA.MetricPreOpportunity)-->46(SAM.CommonFA.MetricOpportunity)
35(SAM.CommonFA.PopulationFME)-->45(SAM.CommonFA.MetricPreOpportunity)
41(SAM.CommonFA.MetricCost)-->45(SAM.CommonFA.MetricPreOpportunity)
41(SAM.CommonFA.MetricCost)-->44(SAM.CommonFA.MetricOutliers)
39(SAM.CommonFA.ChargeDetails)-->43(SAM.CommonFA.CommonFAFinancePicuDays)
39(SAM.CommonFA.ChargeDetails)-->42(SAM.CommonFA.CommonFAFinanceNurseryDays)
39(SAM.CommonFA.ChargeDetails)-->41(SAM.CommonFA.MetricCost)
39(SAM.CommonFA.ChargeDetails)-->40(SAM.CommonFA.OPVisits)
35(SAM.CommonFA.PopulationFME)-->39(SAM.CommonFA.ChargeDetails)
36(SAM.CommonFA.PremetricCost)-->39(SAM.CommonFA.ChargeDetails)
{% endmermaid %}

{% mermaid sequenceDiagram %}
participant Alice
participant Bob
participant John as John<br/>Second Line
Alice ->> Bob: Hello Bob, how are you?
Bob-->>John: How about you John?
Bob--x Alice: I am good thanks!
Bob-x John: I am good thanks!
Note right of John: Bob thinks a long<br/>long time, so long<br/>that the text does<br/>not fit on a row.
Bob-->Alice: Checking with John...
alt either this
Alice->>John: Yes
else or this
Alice->>John: No
else or this will happen
Alice->John: Maybe
end
par this happens in parallel
Alice -->> Bob: Parallel message 1
and
Alice -->> John: Parallel message 2
end
{% endmermaid %}

{% note success %}
success 提示块标签
{% endnote %}

{% note info %}
info 提示块标签
{% endnote %}

{% note warning %}
warning 提示块标签
{% endnote %}

{% note danger %}
danger 提示块标签
{% endnote %}

> tabs

{% tabs test1 %}
<!-- tab base1 -->
**选项卡 1**
<!-- endtab -->
<!-- tab base2 -->
**选项卡 2**
<!-- endtab -->
<!-- tab base3 -->
**选项卡 3** 名字为A
<!-- endtab -->
{% endtabs %}
primary，success，info，warning，danger

{% label default@default %}
{% label primary@primary %}
{% label success@success %}
{% label info@info %}
{% label warning@warning %}
{% label danger@danger %}

{% echarts 400 '85%' %}
{
    tooltip : {
        trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    legend: {
        data:['利润', '支出', '收入']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis : [
        {
            type : 'value'
        }
    ],
    yAxis : [
        {
            type : 'category',
            axisTick : {show: false},
            data : ['周一','周二','周三','周四','周五','周六','周日']
        }
    ],
    series : [
        {
            name:'利润',
            type:'bar',
            itemStyle : {
                normal: {
                    label: {show: true, position: 'inside'}
                }
            },
            data:[200, 170, 240, 244, 200, 220, 210]
        },
        {
            name:'收入',
            type:'bar',
            stack: '总量',
            itemStyle: {
                normal: {
                    label : {show: true}
                }
            },
            data:[320, 302, 341, 374, 390, 450, 420]
        },
        {
            name:'支出',
            type:'bar',
            stack: '总量',
            itemStyle: {normal: {
                label : {show: true, position: 'left'}
            }},
            data:[-120, -132, -101, -134, -190, -230, -210]
        }
    ]
};
{% endecharts %}
