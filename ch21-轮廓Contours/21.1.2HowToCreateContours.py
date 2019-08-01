# -*- coding: utf-8 -*-
# __author__ = 'corvin'

"""
21.1.2 怎样绘制轮轮廓.py:
函数 cv2.drawContours() 可以 用来绘制 轮廓。它可以根据你提供 的 界点绘制任何形状。
第一个参数是原始图像
第二个参数是 轮廓 一 个 Python 列表。
第三个参数是 轮廓的索引
在绘制独立 轮廓是很有用 当 设置为 -1 时绘制所有轮廓 。
接下来的参数是 轮廓的颜色和厚度等。
"""

import numpy as np
import cv2

im = cv2.imread('../data/cards.png')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow('imgray', imgray)
# cv2.waitKey(2000)

# threshold函数有两个返回值，其中第二个返回值（这里是mask）是二值化后的灰度图。当我们指定了阈值参数thresh，第一个返回值ret就是我们指定的thresh。换句话说，我们可以不指定阈值参数thresh。
# 将灰度图img2gray中灰度值小于244的点置0，灰度值大于244的点置255
ret, thresh = cv2.threshold(imgray, 244, 255, 0)
print("ret: %s" % ret, "thresh: %s" % thresh)

img, contour, hiserarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print('len(contours):', len(contour))

contours = [cnt for cnt in contour if cv2.contourArea(cnt) > 200] # 过滤太小的contour
print("过滤太小的contours:", len(contours))

# 它的第一个参数是原始图像，第二个参数是轮廓，一个Python 列表。第三个参数是轮廓的索引（在绘制独立轮廓是很有用，当设置为-1 时绘制所有轮廓）。接下来的参数是轮廓的颜色和厚度等。
# cv2.drawContours(imgray, contours, -1, (0, 0,255), 3)
cv2.drawContours(im, contours, -1, (255, 0, 0), 3)

if len(contours) > 4:
    # To gdraw an individual contour, say 4th contour:
    # drawContours(image, contours, contourIdx, color, thickness=None, lineType=None, hierarchy=None, maxLevel=None, offset=None)
    # 绘制独立 轮廓 如第四个 轮廓
    cv2.drawContours(image=im, contours=contours, contourIdx=3,  color=(0, 0, 255), thickness=3)
    # But most of time, below method will be useful:
    cnt = contours[4]
    cv2.drawContours(im, [cnt], 0, (0, 0, 255), 3)

# 第一个contour
print('contour[0]: ', contours[0])
cv2.drawContours(imgray, contours[0], 0, (0, 0, 255), 3)
'''
 这个参数如果 设置为 cv2.CHAIN_APPROX_NONE 
 所有的边界点 都 会被存储。但是我们真的需要那么多点吗 ？
 例如 当我们找的边界是一条直线时。你需要直线上所有的点来表示直线吗 ？
 不是的 我们只需要1 条直线 的两个端点而已。 
 就是 cv2.CHAIN_APPROX_SIMPLE  做的。它会
将 轮廓上的冗余点 去掉， 压缩 轮廓 ，从而节省内存开支。
'''
cv2.imshow('drawContours', im)
cv2.imshow('drawContours-', imgray)
cv2.waitKey(0)


"""
findContours( InputOutputArray image, OutputArrayOfArrays contours,
                              OutputArray hierarchy, int mode,
                              int method, Point offset=Point());

第一个参数：image，单通道图像矩阵，可以是灰度图，但更常用的是二值图像，一般是经过Canny、拉普拉斯等边
                     缘检测算子处理过的二值图像；

第二个参数：contours，定义为“vector<vector<Point>> contours”，是一个向量，并且是一个双重向量，向量
           内每个元素保存了一组由连续的Point点构成的点的集合的向量，每一组Point点集就是一个轮廓。  
           有多少轮廓，向量contours就有多少元素。

第三个参数：hierarchy，定义为“vector<Vec4i> hierarchy”，先来看一下Vec4i的定义：
                           typedef    Vec<int, 4>   Vec4i;                                                                                                                                       
           Vec4i是Vec<int,4>的别名，定义了一个“向量内每一个元素包含了4个int型变量”的向量。
           所以从定义上看，hierarchy也是一个向量，向量内每个元素保存了一个包含4个int整型的数组。
           向量hiararchy内的元素和轮廓向量contours内的元素是一一对应的，向量的容量相同。
           hierarchy向量内每一个元素的4个int型变量——hierarchy[i][0] ~hierarchy[i][3]，分别表示第
        i个轮廓的后一个轮廓、前一个轮廓、父轮廓、内嵌轮廓的索引编号。如果当前轮廓没有对应的后一个
        轮廓、前一个轮廓、父轮廓或内嵌轮廓的话，则hierarchy[i][0] ~hierarchy[i][3]的相应位被设置为
        默认值-1。

第四个参数：int型的mode，定义轮廓的检索模式：
           取值一：CV_RETR_EXTERNAL只检测最外围轮廓，包含在外围轮廓内的内围轮廓被忽略
           取值二：CV_RETR_LIST   检测所有的轮廓，包括内围、外围轮廓，但是检测到的轮廓不建立等级关
                  系，彼此之间独立，没有等级关系，这就意味着这个检索模式下不存在父轮廓或内嵌轮廓，
                  所以hierarchy向量内所有元素的第3、第4个分量都会被置为-1，具体下文会讲到
           取值三：CV_RETR_CCOMP  检测所有的轮廓，但所有轮廓只建立两个等级关系，外围为顶层，若外围
                  内的内围轮廓还包含了其他的轮廓信息，则内围内的所有轮廓均归属于顶层
           取值四：CV_RETR_TREE， 检测所有轮廓，所有轮廓建立一个等级树结构。外层轮廓包含内层轮廓，内
                   层轮廓还可以继续包含内嵌轮廓。

第五个参数：int型的method，定义轮廓的近似方法：
           取值一：CV_CHAIN_APPROX_NONE 保存物体边界上所有连续的轮廓点到contours向量内
           取值二：CV_CHAIN_APPROX_SIMPLE 仅保存轮廓的拐点信息，把所有轮廓拐点处的点保存入contours
                   向量内，拐点与拐点之间直线段上的信息点不予保留
           取值三和四：CV_CHAIN_APPROX_TC89_L1，CV_CHAIN_APPROX_TC89_KCOS使用teh-Chinl chain 近
                   似算法

第六个参数：Point偏移量，所有的轮廓信息相对于原始图像对应点的偏移量，相当于在每一个检测出的轮廓点上加
            上该偏移量，并且Point还可以是负值！

"""














