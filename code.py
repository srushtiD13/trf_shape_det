import cv2
import numpy as np
sq=0
tr=0
ci=0
pe=0

img1=cv2.imread('t2.jpg')
img1=cv2.resize(img1,(600,500))
cv2.imshow('original',img1)

img2=cv2.GaussianBlur(img1,(5,5),0)
img=cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)
lower = np.array([37, 50, 80])
upper= np.array([70,255,255])#Neon color mask..DO NOT CHANGE
mask = cv2.inRange(img, lower, upper)
blurred_frame = cv2.GaussianBlur(mask, (7, 7), 0)
canny = cv2.Canny(blurred_frame, 100, 150)

contours = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
font = cv2.FONT_HERSHEY_TRIPLEX
for index,cnt in enumerate(contours):

        app = cv2.approxPolyDP(cnt, 0.01* cv2.arcLength(cnt, True), True)
        cX = cv2.approxPolyDP(app, 0, True).ravel()[0]
        cY = cv2.approxPolyDP(app, 0, True).ravel()[1]
        fcX=cX-16
        fcY=cY+16
        print(len(app))

        if len(app) == 4 and sq==0:
            cv2.putText(img1, "Square", (fcX, fcY), font, 1, 180)
            sq=1

        if len(app)== 6 and tr==0:
            cv2.putText(img1, "Triangle", (fcX, fcY), font, 1, 180)
            tr=1

        if len(app) == 12 and ci==0:
            cv2.putText(img1, "Circle", (fcX, fcY), font, 1, 180)
            ci=1

        if len(app) == 8 and pe==0:
           cv2.putText(img1, "Pentagon", (fcX, fcY), font, 1, 180)
           pe=1





cv2.imshow('final',img1)
cv2.waitKey(0)
cv2.destroyAllWindows



