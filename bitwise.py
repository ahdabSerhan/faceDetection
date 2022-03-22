from cmath import rect
import cv2.cv2 as cv
import numpy as np

blank=np.zeros((400,400),dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)


#Bitwise AND -- return the iintersection between two images
bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow('AND',bitwise_and)


#bitwise OR - return both the intersection as non intersection regions
bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow('Or',bitwise_or)

#bitwise XOR - return the non intersecting region 
bitwise_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow('XOR',bitwise_xor)

#bitwise Not - inert the binary colors
bitwise_not=cv.bitwise_not(rectangle)
cv.imshow('Rectangle Not',bitwise_not)

cv.waitKey(0)