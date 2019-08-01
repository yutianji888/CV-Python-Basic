# -*- coding: utf-8 -*-
# __author__ = 'corvin'

"""
首先我们看看如何使用 Numpy 进行傅里叶变换。 Numpy 中的 FFT 包
可以帮助我们实现快速傅里叶变换。函数 np.fft.fft2() 可以对信号进行频率转
换，输出结果是一个复杂的数组。本函数的第一个参数是输入图像，要求是灰
度格式。第二个参数是可选的, 决定输出数组的大小。输出数组的大小和输入图
像大小一样。如果输出结果比输入图像大，输入图像就需要在进行 FFT 前补
0。如果输出结果比输入图像小的话，输入图像就会被切割。
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/messi5.jpg', 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
"""
现在我们得到了结果，频率为 0 的部分（直流分量）在输出图像的左上角。
如果想让它（直流分量）在输出图像的中心，我们还需要将结果沿两个方向平
移 N/2 。函数 np.fft.fftshift() 可以帮助我们实现这一步。（这样更容易分析）。
进行完频率变换之后，我们就可以构建振幅谱了。
"""
rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)
fshift[crow - 30: crow + 30, ccol - 30: ccol + 30] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
# 取绝对值
img_back = np.abs(img_back)

plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(img_back, cmap='gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
plt.show()

"""
上图的结果显示高通滤波其实是一种边界检测操作。这就是我们在前面图
像梯度那一章看到的。同时我们还发现图像中的大部分数据集中在频谱图的低
频区域。我们现在已经知道如何使用 Numpy 进行 DFT 和 IDFT 了，接着我
们来看看如何使用 OpenCV 进行这些操作。
如果你观察仔细的话，尤其是最后一章 JET 颜色的图像，你会看到一些不
自然的东西（如我用红色箭头标出的区域）。看上图那里有些条带装的结构，这
被成为振铃效应。这是由于我们使用矩形窗口做掩模造成的。这个掩模被转换
成正弦形状时就会出现这个问题。所以一般我们不适用矩形窗口滤波。最好的
选择是高斯窗口
"""




















