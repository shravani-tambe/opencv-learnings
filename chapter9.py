import cv2

#FACE DETECTION 

'''Take a bunch of positives -> images of faces 
bunch of negatives -> anything but faces 
train on these positives and negatives 
=> xml file obtained'''

faceCascade= cv2.CascadeClassifier("images/haarcascades/haarcascade_frontalface_default.xml")
img = cv2.imread('images/lena.png')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

'''for live webcam feed: 
    cap = cv2.VideoCapture(0)
    success, img = cap.read()
    
    if not success:
        print("Error: Couldn't read frame from webcam.")
        break
'''

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow("Result", img)
cv2.waitKey(0)