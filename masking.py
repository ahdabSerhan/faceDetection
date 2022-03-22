import cv2.cv2 as cv
import numpy as np

img=cv.imread('Photos/cats.jpg')
# cv.imshow('Cats',img)


blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank img',blank)

mask=cv.circle(blank,(img.shape[1]//2, img.shape[0]//2), 100, 255,-1)
cv.imshow('mask',mask)

msaked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked',msaked)

cv.waitKey(0)