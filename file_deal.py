# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    it mainly use to blog files

usage:
    python file_deal.py

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2019/5/29"
    __mail__ = "mingliang.gao@qunar.com"
------------------------------------------------
"""
import os
import sys
import time
import shutil
import logging

from shutil import ignore_patterns


logging.basicConfig(level=logging.DEBUG,
                    datefmt='%Y/%m/%d %H:%M:%S',
                    format='%(asctime)s || %(filename)s【%(levelname)s】- %(message)s')

LOG = logging.getLogger(__name__)

BASE_DIR_NAME = 'bfile'
PUBLIC_DIR_NAME = 'public'


file_mapping = {
    'love': 'love',
    'images': 'images',
    'publicfiles': 'publicfiles',
}


def get_cur_dir():
    """
    get current file dir
    :return: path
    """
    return os.path.abspath(os.path.dirname(os.path.abspath(__file__)))


def main():
    cur_dir = get_cur_dir()
    l = len(file_mapping)
    start = 1
    for k, v in file_mapping.items():
        if not k or not v:
            continue
        src_dir = os.path.join(cur_dir, BASE_DIR_NAME, v)
        tar_dir = os.path.join(cur_dir, PUBLIC_DIR_NAME, v)
        if os.path.exists(tar_dir):
            shutil.rmtree(tar_dir)
        shutil.copytree(src_dir,
                        tar_dir,
                        ignore=ignore_patterns('*.pyc', 'tmp*'))
        partion = start * 100 / l
        # print("\r")
        LOG.info('======> % s' % k)
        a = "#" * int(partion) + " " * (100-int(partion)) + "["+str(partion) + "%"+"]"
        sys.stdout.write("\r%s" % a)
        sys.stdout.flush()
        time.sleep(0.8)
        start += 1

if __name__ == '__main__':
    main()
