'''# open-cv library is installed as cv2 in python
# import cv2 library into this program'''
import cv2

# import numpy library as np into this program
import numpy as np

# read an image using imread() function of cv2
# we have to  pass only the path of the image

img = cv2.imread(r'../Images/6_scenary.jpg')

# displaying the image using imshow() function of cv2
# In this : 1st argument is name of the frame
# 2nd argument is the image matrix
cv2.imshow('Original Image',img)
print()
# print shape of the image matrix
# using shape attribute
print("Original Image Shape:",img.shape)

# assigning number of rows, coulmns and
# planes to the respective variables
row,col,plane = img.shape

# give value by which you want to resize an image
# here we want to resize an image as one half of the original image
x, y = 2, 2

# assign Blue plane of the BGR image
# to the blue_plane variable
blue_plane = img[:,:,0]

# assign Green plane of the BGR image
# to the green_plane variable
green_plane = img[:,:,1]

# assign Red plane of the BGR image
# to the red_plane variable
red_plane = img[:,:,2]

# we take one-half pixel of rows and columns from
# each plane respectively so that, it is one-half of image matrix.

# here we take alternate row,column pixel of blue plane.
resize_blue_plane = blue_plane[1::x,1::x]

# here we take alternate row,column pixel of green plane.
resize_green_plane = green_plane[1::x,1::x]

# here we take alternate row,column pixel of red plane.
resize_red_plane = red_plane[1::x,1::x]

# here image is of class 'uint8', the range of values  
# that each colour component can have is [0 - 255]

# create a zero matrix of specified order of 3-dimension
resize_img = np.zeros((row//x, col//y, plane),np.uint8)

# assigning resized blue, green and red plane of image matrix to the
# corresponding blue, green, red plane of resize_img matrix variable.
resize_img[:,:,0] = resize_blue_plane
resize_img[:,:,1] = resize_green_plane
resize_img[:,:,2] = resize_red_plane

cv2.imshow('Resized Image',resize_img)

print("Resized Image Shape:",resize_img.shape)
img=resize_img
recon_img=img
cv2.waitKey(0)

cv2.destroyAllWindows()
if img is not None and img.any():
  print("\nDefault name of new image is: '6_new_resized.jpg' , if no input given. \n")
  in_n=input("Enter name of new Image : 6_new_")


  if in_n==None:
    s="../Images/6_new_resized.jpg"
    cv2.imwrite(s, recon_img)
    q='6_new_resized.jpg'
  else:
    s="../Images/6_new_"+in_n+".jpg"
    if s=="../Images/6_new_.jpg":
      s='../Images/6_new_resized.jpg'
    cv2.imwrite(s,recon_img)
    q="6_new_"+in_n+".jpg"
  if q=="6_new_.jpg":
     q='6_new_resized.jpg'
  print('Filtered image saved as: ',q)