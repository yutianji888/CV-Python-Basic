# -*- coding: utf-8 -*-
# __author__ = 'corvin'

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/home.jpg')
color = ('b', 'g', 'r')
# 对一个列表或数组既要遍历索引又要遍历元素时
# 使用内置 enumerrate 函数会有更加直接 优美的做法
# enumerate 会将数组或列表组成一个索引序列。
# 使我们再获取索引和索引内容的时候更加方便

for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])

plt.show()

"""
其中第一个参数必须用方括号括起来。
第二个参数是用于计算直方图的通道，这里使用灰度图计算直方图，所以就直接使用第一个通道；

第三个参数是Mask，这里没有使用，所以用None。

第四个参数是histSize，表示这个直方图分成多少份（即多少个直方柱）。第二个例子将绘出直方图，到时候会清楚一点。

第五个参数是表示直方图中各个像素的值，[0.0, 256.0]表示直方图能表示像素值从0.0到256的像素。

最后是两个可选参数，由于直方图作为函数结果返回了，所以第六个hist就没有意义了（待确定）

最后一个accumulate是一个布尔值，用来表示直方图是否叠加。

彩色图像不同通道的直方图
--------------------- 
作者：Daetalus 
来源：CSDN 
原文：https://blog.csdn.net/sunny2038/article/details/9097989 
版权声明：本文为博主原创文章，转载请附上博文链接！
"""













