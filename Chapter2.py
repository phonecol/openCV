# Basic Functions
import numpy as np
import cv2

img = cv2.imread("100ppm.png")
print(img)
kernel = np.ones((5,5), np.uint8)

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1 )
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("HSV Image", imgHSV)
# cv2.imshow("Blur Image", imgBlur)
# cv2.imshow("Canny Image", imgCanny)
colorHSV = imgHSV[10,10]
print(colorHSV)
color = img[10,10]
print(color)
# cv2.imshow("Dialation Image", imgDialation)
# cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
