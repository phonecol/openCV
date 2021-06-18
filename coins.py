import cv2
from matplotlib import pyplot as plt

img = cv2.imread("100ppm.png")

img_color =     cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)

ret, thresh2 = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

ret, thresh3 = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY + cv2.THRESH_TRIANGLE)

plt.figure("inv")
plt.imshow(thresh, cmap="gray")
plt.figure("otsu")
plt.imshow(thresh2, cmap="gray")
plt.figure("triangle")
plt.imshow(thresh3, cmap="gray")
plt.figure("Grayscale")
plt.imshow(gray, cmap="gray")

plt.show()