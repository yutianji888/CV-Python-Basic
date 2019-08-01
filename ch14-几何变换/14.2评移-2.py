# -*- coding: utf-8 -*-
# __author__ = 'corvin'

"""
平移-2.py:平移就是将对 换一个位置。如果你 沿 (x, y) 方向移动
移动的距离 是 (tx,ty)
"""


import cv2
import numpy as np

img = cv2.imread('../data/messi5.jpg', 0)
rows, cols = img.shape
print(rows, cols)
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("img", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

















