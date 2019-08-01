# -*- coding: utf-8 -*-
# __author__ = 'corvin'

import cv2

# img = cv2.imread('messi5.jpg', 0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


temp = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)#灰色转RGB



