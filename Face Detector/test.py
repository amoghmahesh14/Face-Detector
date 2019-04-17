#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 21:46:00 2019

@author: amogh
"""

import cv2
import numpy as np
        
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyesDetect = cv2.CascadeClassifier('haarcascade_eye.xml')
cam = cv2.VideoCapture(0)

while(True):
    ret,img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,width,height) in faces:
            cv2.rectangle(img,(x,y),(x+width,y+height),(0,255,0),2)
            #(x,y) is the starting point of the circle , (x,y) correspond to (0,0) cell in the matrix
            #(x+width,y+height) is the ending point of the circle , this is (m,n) cell in the matrix
            #(0,255,00) -> (R,G,B) gives color
            # 2 is the thickness
            roi = img[y:y+height, x:x+width]
            eyes = eyeCascade.detectMultiScale(roi)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi,(ex,ey),(ex+ew,ey+eh), 255, 2)

    cv2.imshow("Face Detector",img)
    if(cv2.waitKey(1)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()
