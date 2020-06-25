# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:

usage:
    python blog_requests.py

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2019/9/6"
    __mail__ = "mingliang.gao@qunar.com"
------------------------------------------------
"""

import os
import random
import requests
from gevent import monkey
import gevent
import time


monkey.patch_all()


HTML_REL_DIR = 'public/articles'


def get_cur_dir():
    return os.path.abspath(os.path.dirname(__file__))


class BlogRequests(object):
    def __init__(self):
        self.article_source = os.path.join(get_cur_dir(), HTML_REL_DIR)

    def collect_codes(self):
        """
        get all article codes
        :return: list type
        """
        return os.listdir(self.article_source)

    def _request_url(self, code, run_type):

        refer_url = 'http://pygo2.cn/articles/%s/' % code
        # refer_url = 'http://pygo2.cn/articles/%s/' % code
        url = 'https://busuanzi.ibruce.info/busuanzi?jsonpCallback=BusuanziCallback_558522558688'

        headers = {
            'Referer': refer_url
        }
        print '============================%s============================' % refer_url
        for i in range(1, random.randint(260, 520)):
            resp = requests.get(url=url, headers=headers)
            print '%d : %s' % (i, resp.status_code)
            # print resp.text
            if run_type == 1:
                time.sleep(random.uniform(0.3, 0.8))

    def run(self, run_type=1):
        codes = self.collect_codes()
        print codes
        jobs = list()
        for code in codes:
            if not code:
                continue
            if isinstance(code, unicode):
                code = code.encode('utf-8')

            if run_type == 1:
                jobs.append(gevent.spawn(self._request_url, code, run_type))
            else:
                self._request_url(code, run_type)

        if run_type == 1:
            gevent.joinall(jobs)

        print '-------------end-------------'

if __name__ == '__main__':
    br = BlogRequests()
    br.run(1)
