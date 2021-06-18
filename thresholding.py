# Basic Functions
import numpy as np
import cv2

img = cv2.imread("100ppm.png")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# displayColorImage(img,"Color image")
hsv = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)

gray =cv2.cvtColor(hsv, cv2.COLOR_BGR2GRAY)

(T, threshold) = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
threswithblur = cv2.medianBlur(threshold,15,0)

# (T, thresholdInverse) = cv2.threshold(hsv,100,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
# threswithblur = cv2.medianBlur(thresholdInverse,15,0)

masked = cv2.bitwise_and(img_rgb, img_rgb, mask = threshold)
maskwithblur = cv2.medianBlur(masked,15,0)
cv2.imshow("img", img)
cv2.imshow("gray", hsv)
cv2.imshow("gray", gray)
cv2.imshow("imgrgb", img_rgb)
cv2.imshow("masked", masked)
cv2.waitKey(0)

# cv2.imshow("Dialation Image", imgDialation)
# cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
