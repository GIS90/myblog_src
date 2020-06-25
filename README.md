# PyGo

my first blog.


start
    hexo server -p 8888 --debug --draft

pulic
    hexo g
    python file_deal.py && python tag_cloud.py
    gulp
    hexo d


scripts remark:
    file_deal.py：if execute hexo clean to restore backed-up files
    tag_cloud.py：generate to tags cloud picture
