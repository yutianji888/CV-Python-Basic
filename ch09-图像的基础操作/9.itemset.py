# -*- coding: utf-8 -*-
# __author__ = 'corvin'

import numpy as np
import cv2

img = cv2.imread('../data/messi5.jpg')

print("image.shape: {}".format(img.shape))
px = img[100, 100]
print(px)
blue = img[100, 100, 0]
print(blue)

img[100, 100] = [255, 255, 255]
print(img[100, 100])

# 获取像素值及更好的修改方法
print(img.item(10, 10, 2))
img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2))


































