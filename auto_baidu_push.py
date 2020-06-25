# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    自动化推送blog的url到百度

usage:
    python auto_baidu_push.py

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2019/07/18"
    __mail__ = "mingliang.gao@163.com"

思路：
    获取blog全部的url，生成url.txt文本，使用baidu站点的curl命令进行数据自动化推送，删除url.txt文件。
------------------------------------------------
"""
import os
import shutil


# 本机
HTML_REL_DIR = '/Users/gaomingliang/github/myblog/pygo/public/articles'
# 服务器
# HTML_REL_DIR = '/opt/www/blog/articles'


PUSH_baidu_COMMAND = 'curl -H "Content-Type:text/plain" --data-binary @urls.txt "http://data.zz.baidu.com/urls?site=www.pygo2.cn&token=VqQF08BReWjBB018"'
DOMAIN_TEPM = 'http://www.pygo2.cn/articles'
URL_NAME = 'urls.txt'


def get_cur_dir():
    """
    static method
    用于获取文件执行的当前目录
    """
    return os.path.abspath(os.path.dirname(__file__))


class BlogRequests(object):
    def __init__(self):
        self.article_source = HTML_REL_DIR
        self.cur_dir = get_cur_dir()

    def collect_codes(self):
        """
        get all article codes
        :return: list type
        """
        return os.listdir(self.article_source)

    def generator_url_text(self):
        all_codes = self.collect_codes()
        if not all_codes:
            print '============== not codes'
            return False

        url_file = os.path.join(self.cur_dir, URL_NAME)
        if not os.path.exists(url_file):
            fd = open(url_file, mode="w")
            fd.close()

        with open(url_file, 'w') as f:
            for code in all_codes:
                url = DOMAIN_TEPM + '/%s/' % code
                f.write(url)
                # 换行符
                f.write('\n')
        return url_file

    def run(self):
        url_file = self.generator_url_text()
        if url_file:
            os.system(PUSH_baidu_COMMAND)
        print '-------------end-------------'


if __name__ == '__main__':
    br = BlogRequests()
    br.run()
