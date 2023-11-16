# Import packages

import cv2
print()
import numpy as np

img = cv2.imread('../Images/3_4_turtle.jpg')

print("original image size: ",img.shape) # Print image shape

cv2.imshow("original", img)

# Cropping an image

cropped_image = img[80:280, 150:330]

# Display cropped image

cv2.imshow("cropped", cropped_image)
print("cropped image size: ",cropped_image.shape)

# Save the cropped image

#cv2.imwrite("../Images/4_CroppedImage.jpg", cropped_image)
recon_img=cropped_image
cv2.waitKey(0)

cv2.destroyAllWindows()
if img is not None and img.any():
  print("\nDefault name of new image is: '4_new_cropped.jpg' , if no input given. \n")
  in_n=input("Enter name of new Image : 4_new_")


  if in_n==None:
    s="../Images/4_new_cropped.jpg"
    cv2.imwrite(s, recon_img)
    q='4_new_cropped.jpg'
  else:
    s="../Images/4_new_"+in_n+".jpg"
    if s=="../Images/4_new_.jpg":
      s='../Images/4_new_cropped.jpg'
    cv2.imwrite(s,recon_img)
    q="4_new_"+in_n+".jpg"
  if q=="4_new_.jpg":
     q='4_new_cropped.jpg'
  print('Filtered image saved as: ',q)




