#!/usr/bin/env python3

import numpy as np 
import cv2
import sys

# This is 


def set_waitkey(key):
	is_64bits = sys.maxsize > 2**32
	if is_64bits:
		return cv2.waitKey(key) & 0xFF
	else:
		return cv2.waitKey(key)

# Load in the images. 
up_black = cv2.imread('unknown-pleasures-black.jpg', 1) # greyscale
up_white = cv2.imread('unknown-pleasures-white.png', 1) # greyscale

# Display image
cv2.imshow('White is Right', up_white)
cv2.imshow('Black is Whack', up_black)

k = set_waitkey(0)
if k == 27:	# Wait for ESC key to exit
	cv2.destroyAllWindows()
elif k == ord('s'):
	imwrite('up_black_greyscale.png', up_black)
	imwrite('up_white_greyscale.png', up_white)
	cv2.destroyAllWindows()