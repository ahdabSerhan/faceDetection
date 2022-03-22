import cv2.cv2 as cv 
import numpy as np
img=cv.imread('Photos/cats.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

blank=np.zeros(img.shape,dtype='uint8')
# blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# canny=cv.Canny(blur,125,175)
ret, thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
contours, hierarchies =cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(len(contours))
cv.imshow('Thresh',thresh)

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours',blank)


cv.waitKey(0)