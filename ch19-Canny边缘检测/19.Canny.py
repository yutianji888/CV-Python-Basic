# -*- coding: utf-8 -*-
# __author__ = 'corvin'

"""
Canny 边缘检测是一种非常流行的边缘检测算法，是 John F.Canny 在
1986 年提出的。它是一个有很多步构成的算法，我们接下来会逐步介绍。
由于边缘检测很容易受到噪声影响，所以第一步是使用 5x5 的高斯滤波器
去除噪声。
对平滑后的图像使用 Sobel 算子计算水平方向和竖直方向的一阶导数（图
像梯度）（ Gx 和 Gy）。
梯度的方向一般总是与边界垂直。梯度方向被归为四类：垂直，水平，和
两个对角线。

非极大值抑制
在获得梯度的方向和大小之后，应该对整幅图像做一个扫描，去除那些非
边界上的点。对每一个像素进行检查，看这个点的梯度是不是周围具有相同梯
度方向的点中最大的。

滞后阈值
现在要确定那些边界才是真正的边界。这时我们需要设置两个阈值：
minVal 和 maxVal。当图像的灰度梯度高于 maxVal 时被认为是真的边界，
那些低于 minVal 的边界会被抛弃。如果介于两者之间的话，就要看这个点是
否与某个被确定为真正的边界点相连，如果是就认为它也是边界点，如果不是
就抛弃。

OpenCV 中的 Canny 边界检测
在 OpenCV 中只需要一个函数： cv2.Canny()，就可以完成以上几步。
让我们看如何使用这个函数。这个函数的第一个参数是输入图像。第二和第三
个分别是 minVal 和 maxVal。第三个参数设置用来计算图像梯度的 Sobel
卷积核的大小，默认值为 3。最后一个参数是 L2gradient，它可以用来设定
求梯度大小的方程。如果设为 True，就会使用我们上面提到过的方程，否则
使用方程： Edge−Gradient (G) = jG2 xj + jG2 yj 代替，默认值为 False。
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/messi5.jpg',0)
edges = cv2.Canny(img, 180, 320)

cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.subplot(121), plt.imshow(img, cmap='gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(edges, cmap='gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()





















