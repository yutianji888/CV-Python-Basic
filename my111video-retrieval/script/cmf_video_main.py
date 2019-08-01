# -*- coding: utf-8 -*-
# __author__ = 'corvin'


import json
import sys, time
import logging
import os
from os import path
import threading, multiprocessing
import math
from collections import OrderedDict
from multiprocessing import Pool,Manager
from queue import Empty
import you_get
# import socket
# #设置超时时间为30s
# socket.setdefaulttimeout(30)
# from urllib import request
import cv2
import imagehash
from PIL import Image
from cmf_video_url_get import get_linklist_vertica
from cmf_video_fingerprint_export import get_image_export

def _progress(block_num, block_size, total_size):
    '''回调函数
       @block_num: 已经下载的数据块
       @block_size: 数据块的大小
       @total_size: 远程文件的大小
    '''
    sys.stdout.write('\r>> Downloading %s %.1f%%' % (video_name,
                     float(block_num * block_size) / float(total_size) * 100.0))
    sys.stdout.flush()


def video_process(video_path):
    videoname = video_path[video_path.rfind('/') + 1:]
    shortname = videoname[:videoname.rfind('.')]
    # time.sleep(3)
    absolute_path = path.abspath(path.join(path.dirname(__file__), video_path))
    vidcap = cv2.VideoCapture(absolute_path)
    # print("video_path: {0}".format(video_path))
    c = 1
    if vidcap.isOpened():
        reval, frame = vidcap.read()
        # print('reval: {0}'.format(reval))
    else:
        vidcap = cv2.VideoCapture(video_path)
        reval, frame = vidcap.read()
    # # success, image = vidcap.read()
    print('reval: {0}'.format(reval))
    timeF = 3
    flag = 0
    while reval:
        # print(vidcap.isOpened())
        #cap.set(cv2.CAP_PROP_POS_FRAMES,flag) #设置帧数标记
        frameToStart = 5
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, frameToStart)
        ret, im = vidcap.read()#获取图像

        #cv2.waitKey(2000)#延时
        #cv2.imshow('a',im)#显示图像，用在循环中可以播放视频
        if (c % timeF == 0):
            # cv2.imwrite('../data/tmp_image/{}.jpg'.format(shortname), im)#保存图片
            hash_size = 8
            # highfreq_factor = 57600
            # img_size = hash_size * highfreq_factor (1280, 720)
            # img = Image.open('../data/tmp_image/{}.jpg'.format(shortname))
            # img = cv2.imread('../data/tmp_image/{}.jpg'.format(shortname))
            img2 = Image.fromarray(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
            img2_size = img2.size
            # highfreq_factor = 57600
            phash = imagehash.phash(img2, hash_size=hash_size)
            print(phash)
            # return totalFrameNumber, frameRate, img2.size, phash
        # if c > 20:
            break
        c += 1
        cv2.waitKey(1)
    totalFrameNumber = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)  # 获取总帧数
    frameRate = vidcap.get(cv2.CAP_PROP_FPS)  # 获取帧率
    print("视频的名称： {0},获取总帧数: {1}, 获取帧率:{2}".format(videoname, totalFrameNumber, frameRate))
    vidcap.release()
    return totalFrameNumber, frameRate, img2_size, phash
    # print("get image from video done")

def downLoadVideo(url, result_queue):
    os_getpid = os.getpid()
    video_url = 'http://s1.meetsocial.cn/' + str(url)
    video_name = ''.join(url.split('/')[-1:])
    # video_name = str(os_getpid)
    file_path = '../data/video/' + video_name
    absolute_path = path.abspath(path.join(path.dirname(__file__), file_path))
    logging.info(file_path)
    # # request.urlretrieve(video_url, path)
    try:
        if not os.path.isfile(absolute_path):
            sys.argv = ['you-get', '-o', './data/video/', '-O', video_name[:video_name.rfind('.')], video_url]
            you_get.main()
    except Exception as e:
        logging.info(str(e))
        logging.info("Error in url: {0}".format(video_url))
    totalFrameNumber, frameRate, img_size, phash = video_process(file_path)
    print(totalFrameNumber, frameRate, img_size, phash)
    video_dict = OrderedDict()
    value_list = [url, video_url, totalFrameNumber, frameRate, img_size, phash]
    param_list = ["cf_reference_detail", "video_url", "totalFrameNumber", "frameRate", "img_size", "phash"]
    for index, param in enumerate(param_list):
        video_dict[param] = None
        try:
            video_dict[param] = str(value_list[index])
        except:
            pass
    logging.info(video_dict)
    result_queue.put(video_dict)
    try:
        os.remove(absolute_path)
    except:
        pass


#执行方法
# downLoadVideo()
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: python main.py  output_file output_path date')
        sys.exit(1)
    logging.basicConfig(format='%(asctime)s : [%(name)s] : %(levelname)s : %(message)s', level=logging.INFO)
    output_file = sys.argv[1]
    output_path = sys.argv[2]
    file_date = sys.argv[3]
    table_name = "datamining.dmn_cmf_video_fingerprint"

    video_list = get_linklist_vertica(table_name).get_linklist()
    print(len(video_list))
    count = 0
    result_queue = Manager().Queue()
    pool = Pool(4)
    for video in video_list:
        count += 1
        video_name = ''.join(video.split('/')[-1:])
        pool.apply_async(downLoadVideo, (video, result_queue,))
        if count % 20 == 0:
            break
    pool.close()
    with open(output_file, 'w') as output_file1:
        while True:
            try:
                data = result_queue.get(timeout=600)
            except Empty:
                break
            output_file1.write('{}\n'.format(json.dumps(data)))
    output_file1.close()
    pool.join()
    get_image_export(table_name, output_path, file_date).run()
    logging.info("===============================ALL DONE===========================")



































