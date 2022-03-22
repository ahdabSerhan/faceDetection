import cv2.cv2 as cv 
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
# cv.imshow('Blank',blank)


# 1. paint the image to certain color
blank[200:300,300:400]= 0,0,225
# cv.imshow('Green',blank)


img=cv.imread('Photos/cat.jpg')
# cv.imshow('Cat',img)
# Draw REctangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1   )
# cv.imshow('rectangle',blank)

# draw Circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),240,(0,0,255),thickness=3)
# cv.imshow('Circle',blank)

# draw Line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3)
# cv.imshow('Line',blank)

# draw text
cv.putText(blank,'Naser Abu Tayea',(100,300),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('Text',blank)

cv.waitKey(0)