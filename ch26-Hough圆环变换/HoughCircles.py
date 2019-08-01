# -*- coding: utf-8 -*-
# __author__ = 'corvin'

"""
一个圆环 需要 3 个参数来确定。所以进行圆环 夫变换的累加器必须是 3 维的
  这样的 效率 就会很低。所以 OpenCV 用来一个比 巧妙的办法 霍夫梯度法 它可以使 用边界的梯度信息。

参数：
image： 8位，单通道图像。如果使用彩色图像，请先转换为灰度。
method：定义检测图像中的圆的方法。目前，唯一实现的方法是cv2.HOUGH_GRADIENT对应于Yuen等。纸。
dp：该参数是累加器分辨率与图像分辨率的反比（详见Yuen等人）。实质上，dp获取越大，累加器数组越小。
minDist：检测到的圆的中心（x，y）坐标之间的最小距离。如果minDist太小，则可能（错误地）检测到与原始相邻的多个圆。如果minDist太大，那么一些圈子根本就不会被检测到。
param1： Yuen等人用于处理边缘检测的梯度值 方法。
param2：该cv2.HOUGH_GRADIENT方法的累加器阈值。阈值越小，检测到的圈子越多（包括虚假圈子）。阈值越大，可能会返回的圈数越多。
minRadius：半径的最小大小（以像素为单位）。
maxRadius：半径的最大大小（以像素为单位）。
"""
import cv2
import numpy as np

img = cv2.imread('../data/OpenCV_Logo_with_text.png', 0)
img = cv2.medianBlur(img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

#HoughCircles(image, method, dp, minDist, circles=None, param1=None, param2=None, minRadius=None, maxRadius=None)
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

circles = np.uint16(np.around(circles))
print(circles)

for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow("detected circles", cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()













