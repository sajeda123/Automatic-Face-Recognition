import cv2
import os
from playsound import playsound
import numpy as np
cam = cv2.VideoCapture(0)
rec=cv2.face.LBPHFaceRecognizer_create();
rec.read("trainner_data/trainner.yml")
detector = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
sampleNum = 0
check = 1
fontface=cv2.FONT_HERSHEY_SIMPLEX
while (True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        sampleNum,conf=rec.predict(gray[y:y+h,x:x+w])
        if (sampleNum==1):
            sampleNum="Prapti"
            if(check==1):
                check += 1
                playsound('prapti.mp3')
                os.system('python send_sms.py')
                break
        elif(sampleNum==2):
            sampleNum="Utpal"
            if (check == 1):
                check += 1
                playsound('utpal.mp3')
                os.system('python send_sms.py')
                break

        elif (sampleNum == 3):
            sampleNum = "saidul"
            if (check == 1):
                check += 1
                playsound('saidul.mp3')
                os.system('python send_sms.py')
                break

        #cv.cv.putText(cv.cv.fromarray(img),str(sampleNum),(x,y+h),font,255)
        cv2.putText(img, str(sampleNum), (x, y + h), fontface, 1, (255, 0, 0), 2);
    cv2.imshow('frame', img)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()