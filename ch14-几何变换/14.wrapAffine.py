# -*- coding: utf-8 -*-
# __author__ = 'corvin'

import cv2
import numpy as np

# 移动了100,50 个像素。
img = cv2.imread('../data/messi5.jpg', 0)
rows, cols = img.shape

M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
有一张图片宽度*高度是300*100,用opencv的img.shape返回的是(100,300,3)，shape返回的是图像的行数，列数，色彩通道数。
易错的地方：
行数其实对应于坐标轴上的y,即表示的是图像的高度
列数对应于坐标轴上的x，即表示的是图像的宽度
也就是说shape返回的是(高度， 宽度) = (y , x)

而img[50,10]是否表示是(x,y)为(50,10)的那个像素呢，其实不是。
与shape的原理相同，它表示的也是(y,x)，即表示第50列第10行的那个元素。

'''