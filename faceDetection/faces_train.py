import os
import cv2.cv2 as cv
import numpy as np

people=['Ben Afflek','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']
DIR=r'C:\Users\Ahdabs\python projects\openCV\Faces\train'
haar_cascade=cv.CascadeClassifier('haar_face.xml')

features=[]
labels=[]  #whos face belong to

def create_train():
    # loop of each folder then loop at each image in that folder then grap the face and add it to train set
     for person in people:
         path=os.path.join(DIR,person)
         label=people.index(person)
         
         for img in os.listdir(path):
             img_path=os.path.join(path,img)
             
             img_array=cv.imread(img_path)
             gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
             
             faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
             cv.imshow('faces_rect ',gray)
             for (x,y,w,h) in faces_rect:
                 faces_roi=gray[y:y+h,x:x+w]
                 features.append(faces_roi)
                 labels.append(label)
             

create_train();
# print(f'Lenght of the features = {len(features)}')
# print(f'Lenght of the labels = {len(labels)}')
# print(f'Features ={features}')

print('Training Done -------------')

#convert features array and labels array to npy array
features=np.array(features, dtype='object')
labels=np.array(labels)



#Train our recognaizer

face_recognizer=cv.face.LBPHFaceRecognizer_create()

#train the recognizer on the features llist and labels list
face_recognizer.train(features,labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy ',features)
np.save('labels.npy ',labels)



