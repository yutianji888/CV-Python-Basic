# -*- coding: utf-8 -*-
# __author__ = 'corvin'

"""
模板匹配是用来在一副大图中搜寻查找模版图像位置的方法。 OpenCV 为
我们提供了函数： cv2.matchTemplate()。和 2D 卷积一样，它也是用模
板图像在输入图像（大图）上滑动，并在每一个位置对模板图像和与其对应的
输入图像的子区域进行比较。OpenCV 提供了几种不同的比较方法（细节请看
文档）。返回的结果是一个灰度图像，每一个像素值表示了此区域与模板的匹配
程度。
如果输入图像的大小是（ WxH），模板的大小是（ wxh），输出的结果
的大小就是（ W-w+1， H-h+1）。当你得到这幅图之后，就可以使用函数
cv2.minMaxLoc() 来找到其中的最小值和最大值的位置了。第一个值为矩
形左上角的点（位置），（ w， h）为 moban 模板矩形的宽和高。这个矩形就是
找到的模板区域了
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/messi5.jpg', 0)
img2 = img.copy()
template = cv2.imread('../data/messi_face.jpg', 0)

w, h = template.shape[::-1]
# All the 6 methods for comparison in a list
# TM_CCOEFF是相关系数匹配； TM_CCOEFF_NORMED是归一化的相关系数匹配；
# TM_CCORR是相关匹配，把模版与图像乘起来，数值越大匹配效果越好， 结果检测出两个目标，一个是最佳匹配，一个是最差匹配。
# TM_CCORR_NORMED是归一化的相关匹配，和上面差不多
# TM_SQDIFF是平方差匹配，最佳匹配等于0，数值越大，匹配效果越差
#  TM_SQDIFF_NORMED是标准平方差匹配，与前者差不多
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    # exec 语句用来执行储存在字符串或文件中的 Python 语句。
    # 例如,我们可以在运行时生成一个包含 Python 代码的字符串,
    # 然后使用 exec 语句执行这些语句。
    # eval 语句用来计算存储在字符串中的有效 Python 表达式
    method = eval(meth)
    print("method: {0}".format(method))
    # Apply template Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(min_val, max_val, min_loc, max_loc)
    # 使用不同的比较方法,对结果的解释不同
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img, top_left, bottom_right, 255, 2)

    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img, cmap='gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle('method: ' + meth)
    plt.show()



















