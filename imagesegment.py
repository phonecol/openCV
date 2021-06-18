from sklearn.datasets import load_sample_images
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread
import cv2
path = "100ppm.png"
original = imread(path)
plt.imshow(original)
# plt.show()

segmented = cv2.cvtColor(original,cv2.COLOR_BGR2HSV)

_, mask = cv2.threshold(segmented, thresh=10, maxval=255, type=cv2.THRESH_BINARY)

plt.imshow(mask)
plt.show()