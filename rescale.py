import cv2.cv2 as cv 
img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat',img)

# just for live video
def changeRes(width,heigh):
    capture.set(3,width)
    capture.set(4,heigh)
    
    
def rescaleFrame(frame, scale=0.75):
    width=int(frame.shape[1]*scale)
    heigh=int(frame.shape[0]*scale)
    dimenstions= (width, heigh)
    
    return cv.resize(frame,dimenstions,interpolation=cv.INTER_AREA)

capture=cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame= capture.read()
    frame_resized=rescaleFrame( frame,)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
  