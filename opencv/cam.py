#-*- coding:utf-8 -*-

import cv2
import numpy as np
import time


path =1
cam = cv2.VideoCapture(path)

while True:
    ret,frame = cam.read()
    cv2.imshow('webcam', frame)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
