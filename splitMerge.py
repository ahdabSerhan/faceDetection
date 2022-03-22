import cv2.cv2 as cv 
import numpy as np
img=cv.imread('Photos/park.jpg')
# cv.imshow('Park',img)

blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank',blank)
b,g,r=cv.split(img)
# cv.imshow('Blue',b)
# cv.imshow('Green',g)
# cv.imshow('Red',r)
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow('Red',red)
cv.imshow('green',green)
cv.imshow('blue',blue)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged=cv.merge([b,g,r])
# cv.imshow('Merged',merged)


cv.waitKey(0)
