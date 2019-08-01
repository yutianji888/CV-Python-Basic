# -*- coding: utf-8 -*-
# __author__ = 'corvin'
"""
Progressive Probabilistic Hough Transform。这个函数是 cv2.HoughLinesP()。
它有两个参数。
• minLineLength - 线的最短长度。比这个短的线都会被忽略。
• MaxLineGap - 两条线段之间的最大间隔，如果小于此值，这两条直线
就被看成是一条直线。
更加给力的是，这个函数的返回值就是直线的起点和终点。
"""
import cv2
import numpy as np

img = cv2.imread('../data/sudoku.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

minLineLength = 100
maxLineGap = 10

lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)
print("Len of lines:", len(lines))
print(lines)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# cv2.imwrite('houghlines5.jpg',img)
cv2.imshow("houghlines3.jpg", img)
cv2.waitKey(0)






















