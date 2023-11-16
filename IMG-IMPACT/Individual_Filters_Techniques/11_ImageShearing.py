import numpy as np
import cv2
import matplotlib.pyplot as plt

# read the input image
img = cv2.imread("../Images/11_apple.jpg")
# convert from BGR to RGB so we can plot using matplotlib
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)




# get the image shape
rows, cols, dim = img.shape

# transformation matrix for Shearing

# shearing applied to x-axis
#M = np.float32([[1, 0.5, 0],
 # [0, 1 , 0],
 # [0, 0 , 1]])

# shearing applied to y-axis
M = np.float32([[1, 0.5, 0],
 [0, 1, 0],
 [0, 0, 1]])

# apply a perspective transformation to the image 
sheared_img = cv2.warpPerspective(img,M,(int(cols*1.5),int(rows*1.5)))





#compare = np.concatenate((img, sheared_img), axis=1) 
#cv2.imshow('Image Sheared', compare)

# Display images using subplots
fig, axes = plt.subplots(1, 2, figsize=(8, 4))

# Disable axis
for ax in axes:
    ax.axis('off')

# Plot original image
axes[0].imshow(img)
axes[0].set_title('Original Image')

# Plot sheared image
axes[1].imshow(sheared_img)
axes[1].set_title('Sheared Image')

# Adjust the layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()





# save the resulting image to disk
#plt.imsave("c_sheared.jpg", sheared_img)
recon_img=sheared_img
img=recon_img
if img is not None and img.any():
  print("\nDefault name of new image is: '11_new_sheared.jpg' , if no input given. \n")
  in_n=input("Enter name of new Image : 11_new_")


  if in_n==None:
    s="../Images/11_new_sheared.jpg"
    plt.imsave(s, recon_img)
    q='11_new_sheared.jpg'
  else:
    s="../Images/11_new_"+in_n+".jpg"
    if s=="../Images/11_new_.jpg":
      s='../Images/11_new_sheared.jpg'
    plt.imsave(s,recon_img)
    q="11_new_"+in_n+".jpg"
  if q=="11_new_.jpg":
     q='11_new_sheared.jpg'
  print('Filtered image saved as: ',q)