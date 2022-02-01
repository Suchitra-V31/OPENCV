#-1 97 58 127 54 255 - gel
#-1 138 92 184 49 219 - oil
oil_color=[-1,138 ,92 ,184, 49 ,219]
oil_lower=[-1,92,49]
oil_upper=[138,184,219]
gel_color=[-1 ,97 ,58 ,127 ,54 ,255]
gel_lower=[-1,58,54]
gel_upper=[97,127,225]
import cv2
import numpy as np
color = int(input("Enter the color(0-oil_color,1-gel_color): "))
cap=cv2.VideoCapture(0)
while True:
    success,img=cap.read()
    img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    if color==0:
        lower=np.array(oil_lower)
        upper=np.array(oil_upper)
    elif color==1:
        lower=np.array(gel_lower)
        upper=np.array(gel_upper)
    mask=cv2.inRange(img_hsv,lower,upper)
    final_img=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('Original Image', img)
    cv2.imshow('HSV Image', img_hsv)
    cv2.imshow('Mask Image', mask)
    cv2.imshow('Result', final_img)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break