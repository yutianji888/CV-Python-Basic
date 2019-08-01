# -*- coding: utf-8 -*-
# __author__ = 'corvin'

"""
一维直方图，之所以称为一维，是因为
我们只考虑了图像的一个特征：灰度值。但是在 2D 直方图中我们就要考虑
两个图像特征。对于彩色图像的直方图通常情况下我们需要考虑每个的颜色
（ Hue）和饱和度（ Saturation）。根据这两个特征绘制 2D 直方图
使用函数 cv2.calcHist() 来计算直方图既简单又方便。如果要绘制颜色
直方图的话，我们首先需要将图像的颜色空间从 BGR 转换到 HSV。（记住，
计算一维直方图，要从 BGR 转换到 HSV）。计算 2D 直方图，函数的参数要
做如下修改：
• channels=[0， 1] 因为我们需要同时处理 H 和 S 两个通道。
• bins=[180， 256]H 通道为 180， S 通道为 256。
• range=[0， 180， 0， 256]H 的取值范围在 0 到 180， S 的取值范围
在 0 到 256
"""
import cv2
import numpy as np

img = cv2.imread('../data/home.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print("hsv length {0}, shape: {1}".format(len(hsv), hsv.shape))

hist = cv2.calcHist([hsv], [0, 1], None, [180, 360], [0, 180, 0, 256])
# Numpy 同样提供了绘制 2D 直方图的函数 np.histogram2d()。
# 绘制 1D 直方图时我们使用的是 np.histogram()。
h, s, v = cv2.split(hsv)
print("h: {0}, s: {1}, v:{2}".format(h.shape, s.shape, v.shape))

hist, xbins, ybins = np.histogram2d(h.ravel(), s.ravel(), [180, 256], [[0, 180], [0, 256]])

print("hist: {0}, xbins: {1}, ybins: {2}".format(hist.shape, xbins.shape, ybins.shape))
















