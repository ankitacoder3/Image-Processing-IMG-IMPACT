# Import packages

import cv2

import numpy as np

img = cv2.imread('Images/3_4_turtle.jpg')

print("original image size: ",img.shape) # Print image shape

cv2.imshow("original", img)

# Cropping an image

cropped_image = img[80:280, 150:330]

# Display cropped image

cv2.imshow("cropped", cropped_image)
print("cropped image size: ",cropped_image.shape)

# Save the cropped image

cv2.imwrite("Images/4_CroppedImage.jpg", cropped_image)

cv2.waitKey(0)

cv2.destroyAllWindows()


