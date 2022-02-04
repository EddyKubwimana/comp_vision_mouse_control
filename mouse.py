import cv2
import time
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import pyautogui as pt
curx=0
cury=0
prevx=0
prevy=0
framex,framey=100,40
feed=cv2.VideoCapture(0)
width=500
height=500
feed.set(3,width)
feed.set(4,height)
detector=HandDetector(maxHands=2,detectionCon=0.8)
start=True

while start:

    _,img=feed.read()
    hands,img=detector.findHands(img,draw=True,flipType=True)
    if hands:

        hand1=hands[0]
        lmList=hand1["lmList"]
        #lenght=detector.findDistance(lmList[8],lmList[8],img)
        x1,y1= lmList[8]
        cv2.rectangle(img,(framex,framey),(width-framex,int(height/2)),(0,255,0),3)

        #print(x,y)
        fingers=detector.fingersUp(hand1)
        x1=np.interp(framex,(0,width-framex),(0,1920))
        y1=np.interp(framey,(0,int(height/2)),(0,1080))
        curx = prevx + (x1 - prevx) / 5
        cury = prevy + (y1 - prevy) / 5
        #print(fingers)
        if fingers[1]==1 and fingers[0]!=1 and fingers[2]!=1:
            mousePosition=pt.moveTo(1920-curx,cury)

        elif fingers[1]==1 and fingers[2]==1:
                click=pt.doubleClick()
        else:
            pass
    prevy,prevy=curx,cury








    cv2.imshow('image',img)
    cv2.waitKey(1)

