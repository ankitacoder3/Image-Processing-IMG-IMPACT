#importing all the required modules

import cv2

import numpy as np

#reading the image whose noise is to be removed using imread() function

img = cv2.imread('../Images/9_person.png')


#using medinaBlur() function to remove the noise from the given image

median = cv2.medianBlur(img, 5)

compare = np.concatenate((img, median), axis=1) 

#displaying the noiseless image as the output on the screen

#side by side comparison

cv2.imshow('Median Filter', compare)

cv2.waitKey(0)

cv2.destroyAllWindows
img=median
recon_img=median
if img is not None and img.any():
  print("\nDefault name of new image is: '9_new_medianfilter.jpg' , if no input given. \n")
  in_n=input("Enter name of new Image : 9_new_")


  if in_n==None:
    s="../Images/9_new_medianfilter.jpg"
    cv2.imwrite(s, recon_img)
    q='9_new_medianfilter.jpg'
  else:
    s="../Images/9_new_"+in_n+".jpg"
    if s=="../Images/9_new_.jpg":
      s='../Images/9_new_medianfilter.jpg'
    cv2.imwrite(s,recon_img)
    q="9_new_"+in_n+".jpg"
  if q=="9_new_.jpg":
     q='9_new_medianfilter.jpg'
  print('Filtered image saved as: ',q)