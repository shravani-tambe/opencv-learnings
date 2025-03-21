import cv2 
import numpy as np

#VIRTUAL PAINT 

#READ WEBCAM : 

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,100)

myColors = [[5, 107, 0, 19, 255, 255],
            [133, 56, 0, 159, 156, 255],
            [57, 76, 0, 100, 255, 255],
            [90,48,0,118,255,255]] #orange purple and green found through colour picker

myColorValues = [[51,153,255],          #BGR values for drawing detected colours 
                 [255,0,255],
                 [0,255,0],
                 [255,0,0]]

myPoints = [] 

def findColor(img, myColors, myColorValues): 
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints=[] #will store all points to draw on => [x, y, colorIndex] 
    
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y=getContours(mask)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
            cv2.circle(img, (x, y), 15, myColorValues[count], cv2.FILLED)
        count +=1
    return newPoints

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y #top of the tip & centre point 

def drawOnCanvas(myPoints,myColorValues, img):
    for point in myPoints:
        cv2.circle(img, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)
        
        '''myPoints: A list of stored points, where each point is in the format [x, y, colorIndex].
        each point = [x, y, colorIndex], where:
        point[0] → x coordinate (horizontal position)
        point[1] → y coordinate (vertical position)
        point[2] → colorIndex (refers to myColorValues)
        
        
        cv2.circle() =>
        img: The image on which the circle is drawn.
        (point[0], point[1]): The (x, y) coordinate of the point.
        10: The radius of the circle.
        myColorValues[point[2]]: The color of the circle, retrieved from myColorValues using colorIndex.
        cv2.FILLED: This fills the circle completely.'''

while True:
    success, img = cap.read()
    if not success:
        break
    imgResult = img.copy()
    newPoints = findColor(imgResult, myColors, myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints, myColorValues, imgResult)
        
    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
