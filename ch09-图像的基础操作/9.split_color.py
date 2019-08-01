# -*- coding: utf-8 -*-
# __author__ = 'corvin'

import cv2
import numpy as np
#拆分及合并图像通道

img=cv2.imread('../data/messi5.jpg')

b,g,r = cv2.split(img)#比较耗时的操作，请使用numpy 索引
print("b: {0}".format(b), "g: {}".format(g), "r {}".format(r))
img=cv2.merge((b, g, r))

b=img[:, :, 0]
#使所有像素的红色通道值都为 0,你不必先拆分再赋值。
# 你可以 直接使用 Numpy 索引,这会更快。
img[:, :, 0] = 0
# OpenCV 中是按 BGR， matplotlib 中是按 RGB 排列
cv2.imwrite(filename='split_color3.jpg', img=img)













