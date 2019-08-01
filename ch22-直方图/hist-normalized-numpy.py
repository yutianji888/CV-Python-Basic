# -*- coding: utf-8 -*-
# __author__ = 'corvin'

"""
想象一下如果一副图像中的大多是像素点的像素值都集中在一个像素值范
围之内会怎样呢？例如，如果一幅图片整体很亮，那所有的像素值应该都会很
高。但是一副高质量的图像的像素值分布应该很广泛。所以你应该把它的直方
图做一个横向拉伸（如下图），这就是直方图均衡化要做的事情。通常情况下这
种操作会改善图像的对比度。
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

#怎样使用 Numpy 来进行直方图均衡化
img = cv2.imread('../data/contrast75.png', 0)
# flatten() 将数组变成一维
hist, bins = np.histogram(img.flatten(), 256, [0, 256])
# 计算累积分布图
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

plt.plot(cdf_normalized, color='b')
plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.show()











