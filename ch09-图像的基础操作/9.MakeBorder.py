# -*- coding: utf-8 -*-
# __author__ = 'corvin'

import cv2
import numpy as np
from matplotlib import pyplot as plt

# 为图像扩边，填充
#如果你想在图像周围创建一个边框，就像相框一样
# 经常在卷积运算或 0 填充时被用到。
BLUE = [255, 0, 0]
img1 = cv2.imread('../data/opencv_logo.png')

replicate = cv2.copyMakeBorder(img1, top=10, bottom=10, left=10, right=10, borderType=cv2.BORDER_REPLICATE)

reflect = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_WRAP)

constant = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE) # value 边界颜色

plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

plt.show()


'''
/******************************************************************************************************************
文件说明:
         copyMakeBorder函数详解
时间地点:
         陕西师范大学 文津楼 2017.5.25
作    者:
         九 月
参考资料:
         1)http://blog.sina.com.cn/s/blog_75e063c101014dol.html
		 2)OpenCv官方文档
函数功能:
         1)这个函数经原图像复制到目标图像的中间。复制的原始图像的左边，右边，上边和下边的区域将使用像
		   素向外填充扩展。这个函数可以简化图像边界的处理
		 2)这个函数把源图像拷贝到目的图像的中央，四面填充指定的像素。
		 3)vCopyMakeBorder（）函数可以复制图像并制作边界，将特定图像轻微变大，然后以各种方式自动填充图
		   像边界，当 Bordertype=IPL_BORDER_REPLICATE时，原始图像边缘的行和列被复制到大图像的边缘，当 
		   Bordertype=IPL_BORDER_CONSTANT时，有一个像素宽的黑色边界。
函数原型:
         void copyMakeBorder(InputArray  src,        //【1】输入图像
		                     OutputArray dst,        //【2】输出图像
							 int top,                //【3】表示对边界每个方向添加的像素个数，就是
							 int bottom,             //     边框的粗细程度
							 int left,               //【4】边界的方向包括上下左右
							 int right, 
							 int borderType,         //【5】表示边界的类型
							                         //【6】表示如果边界的类型是 BORDER_CONSTANT，那么边界的颜色值
							 const Scalar& value=Scalar())
边界的类型有以下几种:
         1)BORDER_REPLICATE:重复，就是对边界的像素进行复制
		 2)BORDER_REFLECT:反射,对感兴趣的图像中的像素在两边进行复制例如:fedcba|abcdefgh|hgfedcb反射
		 3)BORDER_REFLECT_101:反射101:例子：gfedcb|abcdefgh|gfedcba
		 4)BORDER_WRAP:外包装：cdefgh|abcdefgh|abcdefg
		 5)BORDER_CONSTANT:常量复制：例子：iiiiii|abcdefgh|iiiiiii
********************************************************************************************************************/
'''




























