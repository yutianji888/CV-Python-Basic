# -*- coding: utf-8 -*-
# __author__ = 'corvin'

import cv2
import numpy as np

'''
使用 OpenCV 检测程序效率
'''
img1 = cv2.imread('../data/ml.jpg')


e1 = cv2.getTickCount()

for i in range(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)

e2 = cv2.getTickCount()
t = (e2 - e1) / cv2.getTickCount() # 时钟频率 或者 每秒钟的时钟数

print(t)

# Result I got is 5.92764131782617e-09 seconds







