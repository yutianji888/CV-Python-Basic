# -*- coding: utf-8 -*-
# __author__ = 'corvin'

"""
函数 np.fft.fft2() 可以对信号进行频率转
换，输出结果是一个复杂的数组。本函数的第一个参数是输入图像，要求是灰
度格式。第二个参数是可选的, 决定输出数组的大小。输出数组的大小和输入图
像大小一样。如果输出结果比输入图像大，输入图像就需要在进行 FFT 前补
0。如果输出结果比输入图像小的话，输入图像就会被切割。
现在我们得到了结果，频率为 0 的部分（直流分量）在输出图像的左上角。
如果想让它（直流分量）在输出图像的中心，我们还需要将结果沿两个方向平
移 N/2 。函数 np.fft.fftshift() 可以帮助我们实现这一步。（这样更容易分析）。
进行完频率变换之后，我们就可以构建振幅谱了。
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

# simple averaging filter without scaling parameter
mean_filter = np.ones((3, 3))
# creating a gussian filter
x = cv2.getGaussianKernel(5, 10)
gaussian = x * x.T
# different edge detecting filters
# scharr in x-direction
scharr = np.array([[-3, 0, 3],
                   [-10, 0, 10],
                   [-3, 0, 3]])
# sobel in x direction
sobel_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])
# sobel in y direction
sobel_y = np.array([[-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]])
# laplacian
laplacian = np.array([[0, 1, 0],
                      [1, -4, 1],
                      [0, 1, 0]])

filters = [mean_filter, gaussian, laplacian, sobel_x, sobel_y, scharr]
filter_name = ['mean_filter', 'gaussian', 'laplacian', 'sobel_x', 'sobel_y', 'scharr_x']

fft_filters = [np.fft.fft2(x) for x in filters]
fft_shift = [np.fft.fftshift(y) for y in fft_filters]
mag_spectrum = [np.log(np.abs(z) + 1) for z in fft_shift]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(mag_spectrum[i], cmap='gray')
    plt.title(filter_name[i]), plt.xticks([]), plt.yticks([])
plt.show()























