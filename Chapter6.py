import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
imgHor = np.hstack((img,img))

# imgStack = stackImages(0.5,(img,img,img))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow("Horizontal", imgStack)

cv2.imshow("Horizontal", imgGray)
cv2.waitKey(0)
