# -*- coding: utf-8 -*-
# __author__ = 'corvin'
"""
draw最大的轮廓.py:
"""
import cv2
import numpy as np

org = cv2.imread("../data/cards.png")
imgray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
cv2.imshow("imgray", imgray)

# 白色背景
ret, threshold = cv2.threshold(imgray, 244, 255, cv2.THRESH_BINARY_INV) # 把黑白反转
cv2.imshow("after threshold", threshold)

image, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

areas = list()
for i, cnt in enumerate(contours):
    areas.append((i, cv2.contourArea(cnt))) # 面积大小

a2 = sorted(areas, key=lambda d: d[1], reverse=False) # 按面积大小,从大到小排序

cv2.waitKey(0) # 要先按一下键盘
for i, are in a2:
    if are < 150:
        continue
    img22 = org.copy() # 逐个contour显示
    cv2.drawContours(img22, contours, i, (0, 0, 255), 3)
    print(i, are)
    cv2.imshow("drawContours", img22)
    cv2.moveWindow("drawContours", x=img22.shape[1], y=0) # 右边
    k = cv2.waitKey(500)
    if k == ord('q'):
        break


cv2.destroyAllWindows()





















