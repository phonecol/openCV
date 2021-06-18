#Chapter 3: Crop and Resize

import cv2
import numpy as np

img = cv2.imread("resources/lambo.png")

print(img.shape)

imgResize = cv2.resize(img, (1000,200))

imgCropped = img[0:200,200:500]

cv2.imshow("Image", img)

cv2.imshow("Image Cropped", imgCropped)

cv2.imshow("Image Resize", imgResize)

cv2.waitKey(0)