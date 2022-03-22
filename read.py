import cv2.cv2 as cv 
# open new window for the img
# img=cv.imread('Photos/cat.jpg')
# cv.imshow('Cat',img)
# cv.waitKey(0)

# open new window for the video
capture=cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame= capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
