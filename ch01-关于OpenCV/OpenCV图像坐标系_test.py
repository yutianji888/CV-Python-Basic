# -*- coding: utf-8 -*-

"""
OpenCV图像坐标系_test.py:
"""
import cv2
import numpy as np

img = cv2.imread('../data/Lenna.png', cv2.IMREAD_UNCHANGED)
print('img.shape:', img.shape)
logo = cv2.imread('../data/opencv_logo.png', cv2.IMREAD_UNCHANGED)
logo = cv2.resize(logo, (20, 20))
print("logo.shape:", logo.shape)

