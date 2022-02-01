import cv2
from pyzbar.pyzbar import  decode
# pyzbar is. “… a pure Python library that reads one-dimensional barcodes and QR codes using the zbar library
#create a function to decode an image
def decoder(image):
    img_gray=cv2.cvtColor(image,0)
    barcode=decode(img_gray)
    for obj in barcode:
        (x,y,w,h)=obj.rect
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
        barcode_data=obj.data.decode('utf-8')
        barcode_type=obj.type
        print("Barcode: " + barcode_data + " | Type: " + barcode_type)
cap=cv2.VideoCapture(0)
while True:
    sucess,img=cap.read()
    decoder(img)
    cv2.imshow('RESULT',img)
    code=cv2.waitKey(10)
    if code==ord('q'):
        break