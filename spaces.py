
import cv2.cv2 as cv 
import matplotlib.pyplot as plt
img=cv.imread('Photos/park.jpg')
# hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow('hsv image',hsv)
cv.imshow('BGR image openCV',img)
# lab color  
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow('lab image',lab)


#display the image with different library displayer as RGB image
plt.imshow(img)
plt.show()


#BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB image openCV',rgb)

cv.waitKey(0)