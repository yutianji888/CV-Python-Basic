# -*- coding: utf-8 -*-
# __author__ = 'corvin'

import numpy as np
import cv2
from matplotlib import pyplot as plt

print(cv2.__version__, cv2.__doc__)
img = cv2.imread('../../data/messi5.jpg', cv2.IMREAD_UNCHANGED)  # 包括图像的 alpha 通道
rows, cols, ch = img.shape
print('行/高:', rows, '列/宽:', cols, '通道:', ch)

img = cv2.resize(img, (640, 480))

rows, cols, ch = img.shape
print('行/高:', rows, '列/宽:', cols, '通道:', ch)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.threshold会自动找到一个介于两波峰之间的阈值, cv2.THRESH_BINARY_INV:黑白二值反转,
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

plt.imshow(thresh, cmap='gray')
plt.show()














