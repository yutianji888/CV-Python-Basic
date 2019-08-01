# -*- coding: utf-8 -*-
# __author__ = 'corvin'

import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
ret = cap.set(3, 640)
ret = cap.set(4, 480)

plt.ion()
while cap.isOpened():
    ret, frame = cap.read()
    plt.show(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.show()
    plt.pause(1)













