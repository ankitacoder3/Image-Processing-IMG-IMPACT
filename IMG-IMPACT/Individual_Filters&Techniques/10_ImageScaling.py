import cv2

import numpy as np
  

try:
    # Read image from disk.

    img = cv2.imread('Images/10_pig.jpg')
  
    # Get number of pixel horizontally and vertically.

    (height, width) = img.shape[:2]
  
    # Specify the size of image along with interploation methods.

    # cv2.INTER_AREA is used for shrinking, whereas cv2.INTER_CUBIC

    # is used for zooming.

    res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation = cv2.INTER_CUBIC)
  
    # Write image back to disk.
    cv2.imwrite('Images/10_result.jpg', res)

    #showing the images
    cv2.imshow('original image',img)
    cv2.imshow('scaled image',res)    

    
  
except IOError:

    print ('Error while reading files !!!')
