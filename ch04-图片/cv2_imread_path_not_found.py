# -*- coding: utf-8 -*-
# __author__ = 'corvin'

import cv2
import numpy as np
import os
import errno

path = 'messi6.jpg'#不正确的路径，文件不存在
# path = '../data/messi5.jpg'

if not os.path.exists(path):
    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)

img = cv2.imread(path, cv2.IMREAD_UNCHANGED)

cv2.imshow('src', img)
cv2.waitKey(0)













