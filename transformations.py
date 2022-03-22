from configparser import Interpolation
from turtle import left, right, up
import cv2.cv2 as cv 
import numpy as np
img=cv.imread('Photos/park.jpg')
# cv.imshow('Park',img)

def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimentions=(img.shape[1],img.shape[0])   #width and heigh
    return  cv.warpAffine(img,transMat,dimentions)

# -x--> left
# -y-->up
# x-->right
# y-->down

translated= translate(img,-100,100)
cv.imshow('Translated',translated)

# Rotation
def rotate(img,angle,rotPoint=None):
    (heigh,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,heigh//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimentions=(width,heigh)
    
    return cv.warpAffine(img,rotMat,dimentions)

rotated=rotate(img,-45)
# cv.imshow('Rotated',rotated)

second_rotated=rotate(img,-90)
# cv.imshow('Rotated second',second_rotated)

resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized',resized)

flipped=cv.flip(img,0)
cv.imshow('Flipped',flipped)

cropped=img[200:400,300:400]
cv.imshow('Cropped',cropped)



cv.waitKey(0)