#!/usr/bin/env python3

from matplotlib import pyplot as plt
import numpy as np 
import cv2
import sys

def set_waitkey(key):
	is_64bits = sys.maxsize > 2**32
	if is_64bits:
		return cv2.waitKey(key) & 0xFF
	else:
		return cv2.waitKey(key)

unkpl = cv2.imread('unknown-pleasures-black.jpg', 0) # Color
ret, unkpl_thresh = cv2.threshold(unkpl, 127, 255, cv2.THRESH_BINARY)

titles = ['Original Image', 'Binary Threshold']
images = [unkpl, unkpl_thresh]

for i in range(len(titles)):
	plt.subplot(1,2,i+1), plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])

plt.show()