import cv2.cv2 as cv

img=cv.imread('../Photos/group 1.jpg')
cv.imshow('Lady',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
# reading the classifier haar cascade xml fille
haar_cascade=cv.CascadeClassifier('haar_face.xml')

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=0)
print(f'Number of faces fount = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected faces ',img)
cv.waitKey(0)