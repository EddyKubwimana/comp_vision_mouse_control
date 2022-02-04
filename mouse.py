import cv2
import time
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import pyautogui as pt
feed=cv2.VideoCapture(0)
width=500
height=500
feed.set(3,width)
feed.set(4,height)
detector=HandDetector(maxHands=2,detectionCon=0.8)
start=True

while start:

    _,img=feed.read()
    img=cv2.cvtColor(img,cv2.COLORMAP_DEEPGREEN)
    hands,img=detector.findHands(img,draw=True,flipType=True)
    if hands:

        hand1=hands[0]
        lmList=hand1["lmList"]
        #lenght=detector.findDistance(lmList[8],lmList[8],img)
        x,y= lmList[8]

        #print(x,y)
        fingers=detector.fingersUp(hand1)
        x1=np.interp(x,(0,width),(0,1920))
        y1=np.interp(y,(40,int(height/2)),(0,1080))

        #print(fingers)
        if fingers[1]==1 and fingers[0]!=1 and fingers[2]!=1:
            mousePosition= pt.moveTo(int(1920-x1),y1)

        elif fingers[1]==1 and fingers[2]==1:
                click=pt.doubleClick()
        else:
            pass

    cv2.imshow('image',img)
    cv2.waitKey(1)

