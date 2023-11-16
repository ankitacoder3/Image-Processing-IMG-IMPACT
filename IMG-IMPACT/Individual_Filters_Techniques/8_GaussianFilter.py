import cv2
import math
import numpy as np
import matplotlib.pyplot as plt

l=[]
v=[]
def show(l, v):
    fig, axes = plt.subplots(1, len(l), figsize=(15, 5))
    titles = [
        "Kernel ({}X{})".format(v[0], v[0]),
        "Image",
        "Padded Image",
        "Output Image using {}X{} Kernel".format(v[1], v[2])
    ]

    for i, img in enumerate(l):
        axes[i].imshow(img, cmap='gray')
        axes[i].set_title(titles[i])
        axes[i].axis('off')

    plt.tight_layout()
    
    

    if img is not None and img.any():
            print("\nDefault name of new image is: '8_new_gaussianfilter.jpg' , if no input given. \n")
            in_n=input("Enter name of new Image : 8_new_")


            if in_n==None:
                s="../Images/8_new_gaussianfilter.jpg"
                plt.tight_layout()
                plt.savefig(s)
                q='8_new_gaussianfilter.jpg'
            else:
                s="../Images/8_new_"+in_n+".jpg"
                if s=="../Images/8_new_.jpg":
                    s='../Images/8_new_gaussianfilter.jpg'
                plt.tight_layout()
                plt.savefig(s)
                q="8_new_"+in_n+".jpg"
            if q=="8_new_.jpg":
                q='8_new_gaussianfilter.jpg'
            print('Filtered image saved as: ',q)
            plt.show()
    

def gaussian_filter():
            image = cv2.imread('../Images/7_8_emoji.png')
            gaussian_blur(image, 5, verbose=False)
            show(l,v)

def convolution(image, kernel, average=False, verbose=False):
    if len(image.shape) == 3:
        print("\nFound 3 Channels : {}".format(image.shape))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print("Converted to Gray Channel. Size : {}".format(image.shape))
    else:
        print("Image Shape : {}".format(image.shape))
 
    print("Kernel Shape : {}".format(kernel.shape))
 
    if verbose:
        plt.imshow(image, cmap='gray')
        plt.title("Image")
        plt.show()
    l.append(image)
 
    image_row, image_col = image.shape
    kernel_row, kernel_col = kernel.shape
 
    output = np.zeros(image.shape)
 
    pad_height = int((kernel_row - 1) / 2)
    pad_width = int((kernel_col - 1) / 2)
 
    padded_image = np.zeros((image_row + (2 * pad_height), image_col + (2 * pad_width)))
 
    padded_image[pad_height:padded_image.shape[0] - pad_height, pad_width:padded_image.shape[1] - pad_width] = image
 
    if verbose:
        plt.imshow(padded_image, cmap='gray')
        plt.title("Padded Image")
        plt.show()
    l.append(padded_image)
 
    for row in range(image_row):
        for col in range(image_col):
            output[row, col] = np.sum(kernel * padded_image[row:row + kernel_row, col:col + kernel_col])
            if average:
                output[row, col] /= kernel.shape[0] * kernel.shape[1]
 
    print("Output Image size : {}".format(output.shape))
 
    if verbose:
        plt.imshow(output, cmap='gray')
        plt.title("Output Image using {}X{} Kernel".format(kernel_row, kernel_col))
        plt.show()
    l.append(output)
    v.append(kernel_row)
    v.append(kernel_col)
 
    return output

def dnorm(x, mu, sd):
    return 1 / (np.sqrt(2 * np.pi) * sd) * np.e ** (-np.power((x - mu) / sd, 2) / 2)
 
 
def gaussian_kernel(size, sigma=1, verbose=False):
    kernel_1D = np.linspace(-(size // 2), size // 2, size)
    for i in range(size):
        kernel_1D[i] = dnorm(kernel_1D[i], 0, sigma)
    kernel_2D = np.outer(kernel_1D.T, kernel_1D.T)
 
    kernel_2D *= 1.0 / kernel_2D.max()
 
    if verbose:
        plt.imshow(kernel_2D, interpolation='none', cmap='gray')
        plt.title("Kernel ( {}X{} )".format(size, size))
        plt.show()
    l.append(kernel_2D)
    v.append(size)
 
    return kernel_2D
 
 
def gaussian_blur(image, kernel_size, verbose=False):
    kernel = gaussian_kernel(kernel_size, sigma=math.sqrt(kernel_size), verbose=verbose)
    return convolution(image, kernel, average=True, verbose=verbose)




if __name__ == "__main__":
	
    gaussian_filter()
    
