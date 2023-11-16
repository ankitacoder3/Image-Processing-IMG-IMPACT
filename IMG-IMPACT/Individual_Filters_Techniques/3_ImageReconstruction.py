from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open('../Images/3_4_turtle.jpg')
img = np.mean(img, 2)

U,s,V = np.linalg.svd(img)

n = 10
S = np.zeros(np.shape(img))
for i in range(0, n):
    S[i,i] = s[i]

recon_img = U @ S @ V

fig, ax = plt.subplots(1, 2)

ax[0].imshow(img)
ax[0].axis('off')
ax[0].set_title('Original')

ax[1].imshow(recon_img)
ax[1].axis('off')
ax[1].set_title(f'Reconstructed n = {n}')

plt.show()
if img is not None and img.any():
  print("\nDefault name of new image is: '3_new_reconstruction.jpg' , if no input given. \n")
  in_n=input("Enter name of new Image : 3_new_")


  if in_n==None:
    s="../Images/3_new_reconstruction.jpg"
    plt.imsave(s, recon_img)
    q='3_new_reconstruction.jpg'
  else:
    s="../Images/3_new_"+in_n+".jpg"
    if s=="../Images/3_new_.jpg":
      s='../Images/3_new_reconstruction.jpg'
    plt.imsave(s,recon_img)
    q="3_new_"+in_n+".jpg"
  if q=="3_new_.jpg":
     q='3_new_reconstruction.jpg'
  print('Filtered image saved as: ',q)

