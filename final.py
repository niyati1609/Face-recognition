import cv2,os
import numpy as np
import pickle
import sqlite3
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path='dataset'

def getprofile(id):
    conn=sqlite3.connect("Facebase.db")
    cmd="SELECT * FROM People WHERE ID="+str(id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile

cam = cv2.VideoCapture(1)
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale=1
fontColor=(255,255,255)
ret,im=cam.read()
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        profile=getprofile(id)
        if(profile!=None):
            cv2.putText(im,str(profile[1]),(x,y+h+30),font,fontScale,fontColor)
            cv2.putText(im,str(profile[2]),(x,y+h+60),font,fontScale,fontColor)
            #cv2.putText(im,str(profile[3]),(x,y+h+90),font,255,fontColor)
    cv2.imshow('im',im) 
    if cv2.waitKey(10) & 0xFF==ord('q'):
       break
cam.release()
cv2.destroyAllWindows()
