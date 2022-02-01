#import the necessary libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt
#load the image
img=cv2.imread('E:\OPEN CV\cartoon image.png')
plt.imshow(img,cmap='gray')
#convert the image to gray
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(img_gray,cmap='gray')
# smoothenning of the image
img_blur=cv2.medianBlur(img_gray,5)
plt.imshow(img_blur,cmap='gray')
#getting the edges  for cartoon effect
get_edge=cv2.adaptiveThreshold(img_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
plt.imshow(get_edge,cmap='gray')
# to get a mask image
mask_img=cv2.bilateralFilter(img,9,300,300)
plt.imshow(mask_img,cmap='gray')
#merge the image
cartoon_img=cv2.bitwise_and(mask_img,mask_img,mask=get_edge)
cv2.imshow('Cartoon Image',cartoon_img)
cv2.waitKey(60)
