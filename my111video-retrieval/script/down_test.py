#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'corvin'
import subprocess
import you_get
import sys
import logging
# video_url = 'http://s1.meetsocial.cn/images/20170616/aa5943bce24048e2.93042910.mp4'
# download_comd = "you-get {}".format(video_url)
# # 在shell中执行并获取标准输出和错误
# p = subprocess.Popen(download_comd, shell=True, cwd='../data/video/')
# p.wait(4000)
# print(result.stdout)
# print(result.stderr)

def download(url, path):
    sys.argv = ['you-get', '-o', path, url]
    you_get.main()

    def video_download(self):
        # 正则表达是判定是否为合法链接
        url = self.url.get()
        path = self.path.get()
        try:
            sys.argv = ['you-get', '-o', path, url]
            you_get.main()
        except Exception as e:
            print(e)
            logging.info()

if __name__ == "__main__":
    video_url = 'http://s1.meetsocial.cn/images/20170616/aa5943bce24048e2.93042910.mp4'
    path = '../data/video/'
    download(video_url, path)
    # download_comd = "you-get {}".format(video_url)
    # 在shell中执行并获取标准输出和错误
    # p = subprocess.Popen(download_comd, shell=True, cwd='../data/video/')


























