# -*- coding: utf-8 -*-
# __author__ = 'corvin'

from urllib import request
import sys
import re
import cv2
import imagehash
from PIL import Image
import os, logging, you_get
import socket
#设置超时时间为30s
socket.setdefaulttimeout(30)

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
    shortname = videoname[:videoname.find('.')]
    vidcap = cv2.VideoCapture(video_path)
    c = 1
    if vidcap.isOpened():
        reval, frame = vidcap.read()
    else:
        reval = False
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    # success, image = vidcap.read()
    timeF = 10
    flag = 0
    while reval:
        # vidcap.set(cv2.CAP_PROP_POS_MSEC, flag)#设置时间标记
        #cap.set(cv2.CAP_PROP_POS_FRAMES,flag) #设置帧数标记
        ret, im = vidcap.read()#获取图像
        #cv2.waitKey(2000)#延时
        #cv2.imshow('a',im)#显示图像，用在循环中可以播放视频
        if (c % timeF == 0):
            cv2.imwrite('../data/tmp_image/{}.jpg'.format(shortname), im)#保存图片
        c += 1
        cv2.waitKey(1)
    vidcap.release()
    print("get image from video done")

def video_process1(video_path):
    videoname = video_path[video_path.rfind('/') + 1:]
    shortname = videoname[:videoname.rfind('.')]
    vidcap = cv2.VideoCapture(video_path)
    c = 1
    if vidcap.isOpened():
        reval, frame = vidcap.read()
    else:
        reval = False
    totalFrameNumber = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)  # 获取总帧数
    frameRate = vidcap.get(cv2.CAP_PROP_FPS)  # 获取帧率
    print("视频的名称： {0},获取总帧数: {1}, 获取帧率:{2}".format(videoname, totalFrameNumber, frameRate))
    # success, image = vidcap.read()
    timeF = 3
    flag = 0
    while reval:
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
            print(img2_size)
            # highfreq_factor = 57600
            phash = imagehash.phash(img2, hash_size=hash_size)
            print(phash)
        # if c > 20:
            break
        c += 1
        cv2.waitKey(1)
    vidcap.release()
    return totalFrameNumber, frameRate, img2_size, phash
    # print("get image from video done")

def downLoadVideo(video_url, video_name):
#    输入的内容有单引号扩起来，表示一个整体
#     url = sys.argv[1]
#     print('链接地址 ：', url)
#     video_url = 'http://s1.meetsocial.cn/' + str(url)
    video_name = ''.join(video_url.split('/')[-1:])
    path = '../data/fb_video/' + video_name
    filepath, _ = request.urlretrieve(video_url, path, _progress)
    # try:
    #     filepath, _ = request.urlretrieve(video_url, path, _progress)
    # except socket.timeout:
    #     count = 1
    #     while count <= 5:
    #         try:
    #             filepath, _ = request.urlretrieve(video_url, path, _progress)
    #             break
    #         except socket.timeout:
    #             err_info = 'Reloading for %d time'%count if count == 1 else 'Reloading for %d times'%count
    #             print(err_info)
    #             count += 1
    #     if count > 5:
    #         print("downloading picture fialed!")
    #
    # print()
    # try:
    #     if not os.path.isfile(path):
    #         sys.argv = ['you-get', '-o', './data/video/', '-O', video_name[:video_name.rfind('.')], video_url]
    #         you_get.main()
    # except Exception as e:
    #     logging.info(str(e))
    #     logging.info("Error in url: {0}".format(video_url))
    totalFrameNumber, frameRate, img_size, phash = video_process1(path)
    print(totalFrameNumber, frameRate, img_size, phash)


#执行方法
# downLoadVideo()
if __name__ == "__main__":
    video_list = [
        # "images/20170511/aa5913cb482ebbd5.86021899.mp4",
        "http://media.meetsocial.cn/video%2Fvideo_fd0bcfe96cf12af2354fe531d7675e25.mp4",
        # "http://s1.meetsocial.cn/images/20170512/aa591553cb7b38f2.06455300.mp4",
        # "http://s1.meetsocial.cn/images/20170512/aa59159aac346676.12411851.mp4",
        # "http://s1.meetsocial.cn/images/20170517/aa591c1d2f696955.00900224.mp4",
        # "http://s1.meetsocial.cn/images/20170519/aa591e5f6500a289.96033893.mp4",
        # "http://s1.meetsocial.cn/images/20170519/aa591e5fbd5eaea0.60716461.mp4",
        # "http://s1.meetsocial.cn/images/20170524/aa5924e6ce8a8ec9.14824401.mp4",
        # "http://s1.meetsocial.cn/images/20170524/aa5924e6ff73d283.03555782.mp4",
        # "http://s1.meetsocial.cn/images/20170524/aa5924e78d3e4285.85848105.mp4",
        # "http://s1.meetsocial.cn/images/20170524/aa5924f403acef71.95893488.mp4",
        # "http://s1.meetsocial.cn/images/20170526/aa5927a23fcf7c30.67239598.mp4",
        # "http://s1.meetsocial.cn/images/20170608/aa5938c0b8365f40.80808859.mp4",
        # "http://s1.meetsocial.cn/images/20170609/aa593a65c45f43c5.82905774.mp4",
        # "http://s1.meetsocial.cn/images/20170609/aa593a66356b53c6.37975398.mp4",
        # "http://s1.meetsocial.cn/images/20170612/aa593e6a38796050.34688283.mp4",
        # "http://s1.meetsocial.cn/images/20170614/aa5940f1c701f7e8.45310200.mp4",
        # "http://s1.meetsocial.cn/images/20170616/aa5943bce24048e2.93042910.mp4",
        # "http://s1.meetsocial.cn/images/20170616/aa5943bce263fee1.03538106.mp4",
        # "http://s1.meetsocial.cn/images/20170616/aa5943bd727522e0.94314995.mp4",
    ]
    # video_url = 'http://s1.meetsocial.cn/images/20170503/aa5909a8949072e7.13219710.mp4'
    for video_url in video_list:
        video_name = ''.join(video_url.split('/')[-1:])
        # downLoadVideo(video_url, '../data/video/' + str(video_url[video_url.rfind('/')+1:]))
        downLoadVideo(video_url, video_name)




































