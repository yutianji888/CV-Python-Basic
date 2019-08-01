# -*- coding: utf-8 -*-
# __author__ = 'corvin'

"""
使用OpenCV进行直方图均衡化.py:
"""
import cv2
import numpy as np

img = cv2.imread('wiki.jpg', 0)

equ = cv2.equalizeHist(img)
res = np.hstack((img, equ)) # stacking images side by side
cv2.imwrite('res.ong', res)




















