'''the convention for x-y coordinates in opencv is such that, the positive x axis and the negative y axis are the positive x-y axis of the plane
refer: https://shorturl.at/Kl2E9'''

#IMAGE RESIZING 

import cv2
import numpy as np

img = cv2.imread("images/lambo.png")
print(img.shape)

imgResize = cv2.resize(img, (900, 600))
print(imgResize.shape)

imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)

cv2.imshow("Image Resize", imgResize)

cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)