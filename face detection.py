import cv2
import os


cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height


face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')




print("\n  Look the camera and wait ...")

count = 0
score=0

while(True):

    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1
        score=score+1
        cv2.waitKey(20000)

        
       # cv2.imwrite("dataset/User." + str(score) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        
        cv2.imshow('image', img)
        os.system("hh.mp3")

    k = cv2.waitKey(100) & 0xff # Escape key
    if k == 27:
        break
    elif count >= 100: # 100 snaps u can increase size
        break
