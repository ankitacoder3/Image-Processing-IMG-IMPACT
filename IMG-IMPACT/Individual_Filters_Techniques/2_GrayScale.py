from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np

input_image = imread(r"../Images/1_2_rover.jpg")

r,g,b = input_image[:,:,0],input_image[:,:,1],input_image[:,:,2]

gamma = 1.04

r_const,g_const,b_const = 0.2126, 0.7152, 0.0722

grayscale_image = r_const * r ** gamma + g_const * g ** gamma + b_const + b **gamma

fig = plt.figure(1)
img1,img2 = fig.add_subplot(121), fig.add_subplot(122)

img1.imshow(input_image)
img2.imshow(grayscale_image, cmap=plt.cm.get_cmap('gray'))

fig.show()
plt.show()
if img2:
  print("\nDefault name of new image is: '2_new_grayscale.jpg' , if no input given. \n")
  in_n=input("Enter name of new Image : 2_new_")


  if in_n==None:
    s="../Images/2_new_grayscale.jpg"
    plt.imsave(s, grayscale_image, cmap='gray')
    q='2_new_grayscale.jpg'
  else:

    s="../Images/2_new_"+in_n+".jpg"
    if s=="../Images/2_new_.jpg":
      s='../Images/2_new_grayscale.jpg'
    plt.imsave(s, grayscale_image, cmap='gray')
    q="2_new_"+in_n+".jpg"
  if q=="2_new_.jpg":
     q='2_new_grayscale.jpg'
  print('Filtered image saved as: ',q)


