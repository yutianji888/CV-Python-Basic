# -*- coding: utf-8 -*-
# __author__ = 'corvin'

"""
findContours2.py:
http://blog.csdn.net/sunny2038/article/details/12889059
"""
import cv2
import numpy as np

img = cv2.imread('contour,jpg', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("thresh", binary)

image, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("contours size:", len(contours))

cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
cv2.imshow("img", img)
cv2.waitKey(0)











