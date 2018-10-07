import cv2
import numpy as np
from matplotlib import pyplot as plt

#code e hamvar saz

img = cv2.imread('5.jpg')
blur = cv2.blur(img, (3, 3))
plt.subplot(121), plt.imshow(img), plt.title('asli')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('hamvar')
plt.xticks([]), plt.yticks([])
plt.show()

img2 = cv2.imread('6.jpg')
blur2 = cv2.blur(img, (3, 3))
plt.subplot(121), plt.imshow(img), plt.title('asli')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur2), plt.title('hamvar')
plt.xticks([]), plt.yticks([])
plt.show()