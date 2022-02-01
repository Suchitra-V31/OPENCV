import cv2
def facedetection(image):
    img_gray=cv2.cvtColor(image,0)
    faceCascade=cv2.CascadeClassifier('E:\OPEN CV\haarcascade_frontalface_default.xml')
    faces=faceCascade.detectMultiScale(img_gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
cap=cv2.VideoCapture(0)
while True:
    success,img=cap.read()
    facedetection(img)
    cv2.imshow('Result',img)
    code=cv2.waitKey(10)
    if code==ord('q'):
        break