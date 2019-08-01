# -*- coding: utf-8 -*-
# __author__ = 'corvin'

"""
ORB 基本是 FAST 关键点检测和 BRIEF 关键点描述器的结合体，并通
过很多修改增强了性能。首先它使用 FAST 找到关键点，然后再使用 Harris
角点检测对这些关键点进行排序找到其中的前 N 个点。它也使用金字塔从而产
生尺度不变性特征。
它使用灰度矩的算法计算出角点的方向。以角点到角点所在（小块）区域
质心的方向为向量的方向。为了进一步提高旋转不变性，要计算以角点为中心
半径为 r 的圆形区域的矩，再根据矩计算除方向。
实验证明， BRIEF 算法的每一位的均值接近 0.5，并且方差很大。 steered_BRIEF
算法的每一位的均值比较分散（均值为 0.5,0.45， 0.35... 等值的关键点数相
当），这导致方差减小。数据的方差大的一个好处是：使得特征更容易分辨。为
了对 steered_BRIEF 算法使得特征的方差减小的弥补和减小数据间的相关性，
用一个学习算法（ learning method）选择二进制测试的一个子集。
在描述符匹配中使用了对传统 LSH 改善后的多探针 LSH。文章中说 ORB
算法比 SURF 和 SIFT 算法快的多， ORB 描述符也比 SURF 好很多。 ORB
是低功耗设备的最佳选择。
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../data/blox.jpg', 0)

# Initiate ORB detector
orb = cv2.ORB_create()
# find the keypoints with ORB
kp = orb.detect(img, None)
# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0), flags=0)

plt.imshow(img2), plt.show()








