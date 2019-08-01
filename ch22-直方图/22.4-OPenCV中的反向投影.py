# -*- coding: utf-8 -*-
# __author__ = 'corvin'

"""
直方图反向投影是可以用来做图像分割，或者在图像中找寻我们感兴
趣的部分。简单来说，它会输出与输入图像（待搜索）同样大小的图像，其中
的每一个像素值代表了输入图像上对应点属于目标对象的概率。用更简单的话
来解释，输出图像中像素值越高（越白）的点就越可能代表我们要搜索的目标
（在输入图像所在的位置）。这是一个直观的解释。直方图投影经常与 camshift
算法等一起使用。
我们应该怎样来实现这个算法呢？首先我们要为一张包含我们要查找目标
的图像创建直方图（在我们的示例中，我们要查找的是草地，其他的都不要）。
我们要查找的对象要尽量占满这张图像（换句话说，这张图像上最好是有且仅
有我们要查找的对象）。最好使用颜色直方图，因为一个物体的颜色要比它的灰
度能更好的被用来进行图像分割与对象识别。接着我们再把这个颜色直方图投
影到输入图像中寻找我们的目标，也就是找到输入图像中的每一个像素点的像
素值在直方图中对应的概率，这样我们就得到一个概率图像，最后设置适当的
阈值对概率图像进行二值化，就这么简单。
"""
import cv2
import numpy as np

roi = cv2.imread('tar.jpg')
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
target = cv2.imread('roi.jpg')
hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)
# calculating object histogram
roihist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

# normalize histogram and apply backprojection
# 归一化 原始图像 结果图像 映射到结果图像中的最小值 最大值 归一化类型
# cv2.NORM_MINMAX 对数组的所有值进行转化 使它们线性映射到最小值和最大值之  间
#  归一化之后的直方图便于显示 归一化之后就成了 0 到 255 之 的数了。
cv2.normalize(roihist, roihist, 0, 255, cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt], [0, 1], roihist, [0, 180, 0, 256], 1)

# Now convolute with circular disc
# 此处卷积可以把分散的点连在一起
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
dst = cv2.filter2D(dst, -1, disc)
# threshold and binary AND
ret, thresh = cv2.threshold(dst, 50, 255, 0)

# 别忘了是三通道图像，因此这里使用 merge 变成 3 通道
thresh = cv2.merge((thresh, thresh, thresh))

# 按位操作
res = cv2.bitwise_and(target, thresh)
res = np.hstack((target, thresh, res))
cv2.imwrite('res.jpg', res)

cv2.imshow('1', res)
cv2.waitKey(0)
cv2.destroyAllWindows()







