from matplotlib import pyplot as plt
import numpy as np
import cv2
## Read image and change the color space
# cv2.imshow('im',imgname)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print('hello')
imgname = "100ppm.png"
img = cv2.imread(imgname)
vis = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# plt.imshow(gray)
# plt.show()
## Get mser, and set parameters
mser = cv2.MSER_create()
# mser.setMinArea(100)
# mser.setMaxArea(8000)
## Do mser detection, get the coodinates and bboxes
# coordinates, bboxes = mser.detectRegions(gray)

regions, _ = mser.detectRegions(gray)
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
cv2.polylines(gray, hulls, 1, (0, 255, 0))

cv2.imshow('img', gray)
cv2.waitKey(0)