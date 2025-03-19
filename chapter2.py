#OPENCV COLOUR CONVENTIONS ARE BGR NOT RGB 
#DISPLAYING IMAGES WITH FILTERS ON

import cv2 
import numpy as np 

img = cv2.imread("images/lena.png")
kernel = np.ones((5, 5), np.uint8) 
'''creates a 5x5 matrix filled with ones, 
hence when expanding edges, the dilation will consider a 5x5 neighbourhood of each pixel''' 

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)

imgCanny = cv2.Canny(img, 100, 100)

imgDilation = cv2.dilate(imgCanny, kernel , iterations = 1) #iterations -> control no. of times that dilation is processed 

imgEroded = cv2.erode(imgDilation, kernel, iterations =1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilated Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)

'''canny and dilation: edge detection produces thin, sharp edges.
dilation thickens these edges, making them more visible and pronounced.'''


cv2.waitKey(0)