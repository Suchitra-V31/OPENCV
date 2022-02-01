import time

import cv2
import numpy as np
cap=cv2.VideoCapture(0)
_,background=cap.read()
time.sleep(2)
_,background=cap.read()
#define all the kernels size
open_kernel = np.ones((5,5),np.uint8)
close_kernel = np.ones((7,7),np.uint8)
dilation_kernel = np.ones((10, 10), np.uint8)

def filter_mask(mask):
    close_mask = cv2.morphologyEx(mask_img, cv2.MORPH_CLOSE, close_kernel)
    open_mask = cv2.morphologyEx(close_mask, cv2.MORPH_OPEN, open_kernel)
    dilation = cv2.dilate(open_mask, dilation_kernel, iterations=1)
    return dilation
while True:
    success,img = cap.read()
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    l = [-1, 38,14]
    u= [64,232, 95]
    lower = np.array(l)
    upper = np.array(u)
    mask_img=cv2.inRange(img_hsv,lower,upper)
    mask=filter_mask(mask_img)
    img_1 = cv2.bitwise_and(background, background, mask=mask)
    inverse_mask=cv2.bitwise_not(mask)
    img_2=cv2.bitwise_and(img,img,mask=inverse_mask)
    comb_img=cv2.add(img_1,img_2)
    cv2.imshow('Original Image',img)
    cv2.imshow('Result',comb_img)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break
