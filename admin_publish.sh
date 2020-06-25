#!/bin/bash


if [ $1 = "all" ];then
    flag=1
elif [ $1 = "ALL" ];then
    flag=1
elif [ $1 = "All" ];then
    flag=1
else
    flag=0
fi



if [ $flag -eq 1 ];then
    hexo clean
    hexo g
    python file_deal.py && python tag_cloud.py
    gulp
else
    hexo g
fi


hexo d --config _config.yml
