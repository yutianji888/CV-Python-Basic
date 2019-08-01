# -*- coding: utf-8 -*-
# __author__ = 'corvin'

"""
两个基本的形态学操作是腐蚀和膨胀。他们
的变体构成了开运算，闭运算，梯度等。

就像土壤侵蚀一样，这个操作会把前景物体的边界腐蚀掉（但是前景仍然
是白色）。这是怎么做到的呢？卷积核沿着图像滑动，如果与卷积核对应的原图
像的所有像素值都是 1，那么中心元素就保持原来的像素值，否则就变为零。
这回产生什么影响呢？根据卷积核的大小靠近前景的所有像素都会被腐蚀
掉（变为 0），所以前景物体会变小，整幅图像的白色区域会减少。这对于去除
白噪声很有用，也可以用来断开两个连在一块的物体等。
"""
import cv2
import numpy as np

img = cv2.imread('j.png', 0)
cv2.imshow('j.png', img)
print(img.shape)

#您可以将内核看作是一个小矩阵，我们在图像上滑动以进行（卷积）操作，例如模糊，锐化，边缘检测或其他图像处理操作。
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)

cv2.imshow('erode', erosion)
cv2.moveWindow('erode', x=img.shape[0], y=0)

cv2.waitKey(0)
cv2.destroyAllWindows()

















