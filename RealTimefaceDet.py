import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('D:\Preps\Python\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('D:\Preps\Python\haarcascade_eye.xml')

img = cv2.imread(r'D:\Preps\Python\anju.jpg')
##cv2.imshow('img',img)
##cv2.waitKey(0)
if img is not None:
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##        cv2.imshow('img',img_gray)
##        cv2.waitKey(0)
###cap = cv2.VideoCapture(0)
##
###while True:
##        frame=cvQueryFrame(cap);
##        if (frame.empty()):
##                break;
##	#ret, img = cap.read()
##        
        faces = face_cascade.detectMultiScale(img_gray,1.3,5)
        for (x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
                roi_gray = img_gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                                                

cv2.imshow('img',img)
####	k = cv2.waitKey(30) & 0xff
####	if k==27:
####		break
####
####cap.release()
cv2.destroyAllWindows()
