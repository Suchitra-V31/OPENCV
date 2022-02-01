import cv2


def cartoon_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.medianBlur(gray, 5)
    get_edge=cv2.adaptiveThreshold(img_blur,225,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,13,3)
    mask_img=cv2.bilateralFilter(image,9,300,300)
    final_img=cv2.bitwise_and(mask_img,mask_img,mask=get_edge)
    cv2.imshow('Result', final_img)

cap=cv2.VideoCapture(0)
while True:
    success,img=cap.read()
    cartoon_image(img)
    code=cv2.waitKey(10)
    if code==ord('q'):
        break