# -*- coding: utf-8 -*-
# __author__ = 'corvin'

"""
使用金字塔进行图像融合
图像金字塔的一个应用是图像融合。例如，在图像缝合中，你需要将两幅
图叠在一起，但是由于连接区域图像像素的不连续性，整幅图的效果看起来会
很差。这时图像金字塔就可以排上用场了，他可以帮你实现无缝连接。

你可以通过阅读后边的更多资源来了解更多关于图像融合，拉普拉斯金字
塔的细节。
实现上述效果的步骤如下：
1. 读入两幅图像，苹果和句子
2. 构建苹果和橘子的高斯金字塔（ 6 层）
3. 根据高斯金字塔计算拉普拉斯金字塔
4. 在拉普拉斯的每一层进行图像融合（苹果的左边与橘子的右边融合）
5. 根据融合后的图像金字塔重建原始图像。
"""
import cv2
import numpy as np, sys

A = cv2.imread('apple.jpg')
B = cv2.imread('orange.jpg')

# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i - 1], GE) #TODO error
    lpA.append(L)


# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i - 1], GE)
    lpB.append(L)

# Now add left and right halves of images in each level
# numpy.hstack(tup)
# Take a sequence of arrays and stack them horizontally
# to make a single array.

LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:cols / 2], lb[:, cols / 2:]))
    LS.append(ls)

# now reconstruct
ls_ = LS[0]
for i in range(1, 6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

# image with direct connecting each half
real = np.hstack((A[:, :cols / 2], B[:, cols / 2:]))

cv2.imwrite('Pyramid_blending20.jpg', ls_)
cv2.imwrite('Direct_blending0.jpg', real)










