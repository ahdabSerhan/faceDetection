import cv2.cv2 as cv 
import numpy as np
img=cv.imread('Photos/cats.jpg')

#Averging
average=cv.blur(img,(3,3))
cv.imshow('Average Blur',average)


#Gaussian Blur
gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian Blur',gauss)

#Median Blur  - more effective in reducing noise
median=cv.medianBlur(img,3)
cv.imshow('Median',median)

#Bilateral 
bilateral=cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral',bilateral)

cv.waitKey(0)