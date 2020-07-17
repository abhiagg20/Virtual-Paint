import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

myColors = [[71,169,66,164,255,224],[0,191,134,14,255,210],[39,157,97,79,255,138]]
myColorValues = [[255,128,255],[0,0,255],[0,204,0]]

myPoints = []

def findColor(img,myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for myColor in myColors:
        lower = np.array(myColor[0:3])
        upper = np.array(myColor[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y = getContours(mask)
        if(x!=0 and y!=0):
            newPoints.append([x,y,count])
        cv2.circle(imgResult, (x,y), 10, myColorValues[count], cv2.FILLED)
        count+=1
        #cv2.imshow(str(myColor[0]),mask)
    return newPoints
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if(area>500):
            #cv2.drawContours(imgResult, cnt, -1, (255,0,0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


while(True):
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if(len(newPoints)!=0):
        for pt in newPoints:
            myPoints.append(pt)
    if(len(myPoints)!=0):
        drawOnCanvas(myPoints, myColorValues)
    cv2.imshow("Result", imgResult)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break