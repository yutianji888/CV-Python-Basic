# -*- coding: utf-8 -*-
# __author__ = 'corvin'

"""
现在我们来做逆 DFT。在前面的部分我们实现了一个 HPF（高通滤波），
现在我们来做 LPF（低通滤波）将高频部分去除。其实就是对图像进行模糊操
作。首先我们需要构建一个掩模，与低频区域对应的地方设置为 1, 与高频区域
对应的地方设置为 0。
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/messi5.jpg', 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
# 这里构建振幅图的公式没学过
magnitude_spectrum = 20 * np.log(np.abs(fshift))

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
