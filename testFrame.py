# coding=utf-8
# 2021.4.2 


from cv2 import cv2
import time
# create camera object, use compute's camera or vedio file
# vedio = cv2.VideoCapture('path of vedio file')
vedio = cv2.VideoCapture(0)
# time.sleep(10)

# get frame
check, frame = vedio.read()
print(frame)

# handle frame
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# show frame
cv2.imshow('kechen', gray)
cv2.waitKey(0)
# ↑ reality get frame, if we add a loop, we can get vedio
vedio.release()