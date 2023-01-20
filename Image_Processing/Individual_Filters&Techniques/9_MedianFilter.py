#importing all the required modules

import cv2

import numpy as np

#reading the image whose noise is to be removed using imread() function

img = cv2.imread('Images/9_person.png')


#using medinaBlur() function to remove the noise from the given image

median = cv2.medianBlur(img, 5)

compare = np.concatenate((img, median), axis=1) 

#displaying the noiseless image as the output on the screen

#side by side comparison

cv2.imshow('Median Filter', compare)

cv2.waitKey(0)

cv2.destroyAllWindows
