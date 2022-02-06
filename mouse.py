import cv2
import time
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import pyautogui as pt
feed = cv2.VideoCapture(0)
width = 500
height = 500
feed.set(3,width)
feed.set(4,height)
smoother = 10
prevX, prevY = 0, 0
curX, curY = 0, 0
detector=HandDetector(maxHands=2,detectionCon=0.8)
start=True

while start:

    _,img = feed.read()
    hands,img=detector.findHands(img,draw=True,flipType=True)
    if hands:

        hand1 = hands[0]
        lmList = hand1["lmList"]
        x, y = lmList[8]

        fingers = detector.fingersUp(hand1)
        x1 = np.interp(x, (0, width), (0,1920))
        y1 = np.interp(y, (40, int(height/2)), (0, 1080))
        curX = prevX+(x1 - prevX)/smoother
        curY = prevY+(y1-prevY)/smoother


        if fingers[1] == 1 and fingers[0] != 1 and fingers[2] != 1:
            mousePosition = pt.moveTo(int(1920-curX), curY)
            prevX=curX
            prevY=curY

        elif fingers[1] == 1 and fingers[2] == 1:
                click = pt.doubleClick()
        else:
            pass


    cv2.imshow('image', img)
    cv2.waitKey(1)

