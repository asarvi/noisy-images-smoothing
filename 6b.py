import cv2
import numpy as np
from matplotlib import pyplot as plt

#code e hamvar saz

img = cv2.imread('5.jpg')
median = cv2.medianBlur(img,3)
plt.subplot(121), plt.imshow(img), plt.title('asli')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(median), plt.title('hamvar')
plt.xticks([]), plt.yticks([])
plt.show()

img = cv2.imread('6.jpg')
median2 = cv2.medianBlur(img,3)
plt.subplot(121), plt.imshow(img), plt.title('asli')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(median2), plt.title('hamvar')
plt.xticks([]), plt.yticks([])
plt.show()