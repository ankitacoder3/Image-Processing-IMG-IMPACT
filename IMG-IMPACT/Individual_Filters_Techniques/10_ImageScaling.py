
import cv2

import numpy as np
  
# Read image from disk.

img = cv2.imread('../Images/10_pig.jpg')
  
# Get number of pixel horizontally and vertically.
(height, width) = img.shape[:2]

scaling_factor=4
res = img[::scaling_factor, ::scaling_factor] #scaling

#showing the images
cv2.imshow('Original Image',img)
cv2.imshow('Scaled Image',res)   

print('\nOriginal Image Shape:',img.shape)
print('Scaled Image Shape:',res.shape)

print('\nIt is scaled by:',1/scaling_factor)

cv2.waitKey(0)

cv2.destroyAllWindows
img=res
recon_img=res
if img is not None and img.any():
  print("\nDefault name of new image is: '10_new_scaled.jpg' , if no input given. \n")
  in_n=input("Enter name of new Image : 10_new_")


  if in_n==None:
    s="../Images/10_new_scaled.jpg"
    cv2.imwrite(s, recon_img)
    q='10_new_scaled.jpg'
  else:
    s="../Images/10_new_"+in_n+".jpg"
    if s=="../Images/10_new_.jpg":
      s='../Images/10_new_scaled.jpg'
    cv2.imwrite(s,recon_img)
    q="10_new_"+in_n+".jpg"
  if q=="10_new_.jpg":
     q='10_new_scaled.jpg'
  print('Filtered image saved as: ',q)
  
