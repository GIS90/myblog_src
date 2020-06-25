# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    词云生成器

usage:
    python tag_cloud.py

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2018/11/21"
    __mail__ = "mingliang.gao@qunar.com"
------------------------------------------------
"""

import os
import re
import jieba
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud
from bs4 import BeautifulSoup


BACKGROUND_NAME = 'public/images/tags_background.png'
HTML_REL_DIR = 'public/articles'
TAR_IMG = 'public/images/blog_tags.jpg'


def get_cur_dir():
    return os.path.abspath(os.path.dirname(__file__))


class TagCloudGenerator(object):
    def __init__(self):
        self.background = os.path.join(get_cur_dir(), BACKGROUND_NAME)
        self.text_source = os.path.join(get_cur_dir(), HTML_REL_DIR)
        self.tar_img = os.path.join(get_cur_dir(), TAR_IMG)

    def get_index_files(self):
        """
        get all index.html file
        :return: list type
        """
        index_files = list()
        pattern = re.compile('index\.html')
        for root, dirs, files in os.walk(self.text_source):
            for f in files:
                f_full = os.path.join(root, f)
                match = pattern.search(f_full)
                index_files.append(f_full) if match else None
        else:
            return index_files

    def get_index_tags(self, index_html):
        """
        get tags of index.html
        :param index_html: index html
        :return: list type
        """
        tags = list()
        if not index_html:
            return tags
        if not os.path.exists(index_html):
            return tags

        def _deal_html_tas():
            soup = BeautifulSoup(open(index_html), 'html.parser', from_encoding='utf-8')
            post_a_tags = soup.find_all('a', attrs={"rel": "tag"})
            if post_a_tags:
                for tag in post_a_tags:
                    tag_text = tag.get_text()
                    tags.append(tag_text.strip())
            return tags

        return _deal_html_tas()

    def collect_tags(self):
        all_tags = list()
        all_indexs = self.get_index_files()
        for index_file in all_indexs:
            if not index_file:
                continue

            tags = self.get_index_tags(index_file)
            print index_file
            all_tags.extend(tags) if tags else None
        else:
            return all_tags

    def run(self):
        all_html_tags = self.collect_tags() * 100
        wl_space_split = " ".join(all_html_tags)
        d = os.path.dirname(__file__)
        tag_background = np.array(Image.open(self.background))
        my_wordcloud = WordCloud(background_color="#CACFD2",
                                 max_words=2000,
                                 font_path="public/publicfiles/fangsong_GB2312.ttf",
                                 mask=tag_background,
                                 stopwords={'企业'},
                                 max_font_size=150,
                                 scale=1,
                                 width=800,
                                 random_state=1).generate(wl_space_split)

        plt.imshow(my_wordcloud)
        plt.axis("off")
        # plt.show()
        my_wordcloud.to_file(self.tar_img)


if __name__ == '__main__':
    tc = TagCloudGenerator()
    tc.run()
