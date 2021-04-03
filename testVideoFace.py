# coding=utf-8
# 2021.4.2 


from cv2 import cv2
import time
# create camera object, use compute's camera or vedio file
# vedio = cv2.VideoCapture('path of vedio file')
vedio = cv2.VideoCapture(0)
# time.sleep(10)
face_cascade = cv2.CascadeClassifier("F:\\ForPython\\OpenCV\\opencv\\data\\haarcascades\\haarcascade_frontalface_default.xml")
while True:
    # get frame
    check, frame = vedio.read()
    # print(frame)

    # handle frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05,  minNeighbors=5) 
    for x,y,w,h in faces:  

        gray = cv2.rectangle(gray, (x,y), (x+w,y+h),(0,255,0),3)  

    resized = cv2.resize(gray, (int(gray.shape[1]),int(gray.shape[0]))) 
    # show frame
    cv2.imshow('kechen', resized)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break
    
vedio.release()
cv2.destroyAllWindows()