import cv2 as cv 

img=cv.imread('Photos/park.jpg')

# converting to grey scale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# blur the image
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# Edge Cascade
canny=cv.Canny(blur,125,175)
cv.imshow('Canny',canny)

# dialating the 
dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilated',dilated)


# Eroding
eroded=cv.erode(dilated,(3,3),iterations=3)
cv.imshow('Eroded',eroded)

resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resize',resized)

cropped=img[50:200,200:400]
cv.imshow('Cropped',cropped)


cv.waitKey(0)