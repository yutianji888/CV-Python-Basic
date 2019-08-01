# -*- coding: utf-8 -*-
# __author__ = 'corvin'

"""
的确在进行完直方图均衡化之后，图片背景的对比度被改变了。但是你再
对比一下两幅图像中雕像的面图，由于太亮我们丢失了很多信息。造成这种结
果的根本原因在于这幅图像的直方图并不是集中在某一个区域（试着画出它的
直方图，你就明白了）。
为了解决这个问题，我们需要使用自适应的直方图均衡化。这种情况下，
整幅图像会被分成很多小块，这些小块被称为“tiles”（在 OpenCV 中 tiles 的
大小默认是 8x8），然后再对每一个小块分别进行直方图均衡化（跟前面类似）。
所以在每一个的区域中，直方图会集中在某一个小的区域中（除非有噪声干
扰）。如果有噪声的话，噪声会被放大。为了避免这种情况的出现要使用对比度
限制。对于每个小块来说，如果直方图中的 bin 超过对比度的上限的话，就把
其中的像素点均匀分散到其他 bins 中，然后在进行直方图均衡化。最后，为了
去除每一个小块之间“人造的”（由于算法造成）边界，再使用双线性差值，对
小块进行缝合。
"""
import numpy as np
import cv2

img = cv2.imread('tsukuba_l.png', 0)
# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)
cv2.imwrite('clahe_2.jpg', cl1)

















