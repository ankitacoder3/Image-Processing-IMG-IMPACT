import numpy as np
import cv2 
import matplotlib.pyplot as plt
import math
from PIL import Image
from matplotlib.image import imread



#1-Colour Filter
def colorfilter(path):
    img = Image.open(path).convert("RGB")
    img.show()
    width,height = img.size

    pixels = img.load()

    def red(r,g,b):
        newr = r
        newg = 0
        newb = 0
        return(newr,newg,newb)

    def darkpink(r,g,b):
        newr = g
        newg = b
        newb = r
        return(newr,newg,newb)

    def skyblue(r,g,b):
        newr = b
        newg = g
        newb = r
        return(newr,newg,newb)

    def lemongreen(r,g,b):
        newr = g
        newg = r
        newb = b
        return(newr,newg,newb)

    def grey(r,g,b):
        newr = (r+g+b)//3
        newg = (r+g+b)//3
        newb = (r+g+b)//3
        return(newr,newg,newb)

    def sepia(r,g,b):
        newr = int((r*.393) + (g*.769) + (b*.189))
        newg = int((r*.349) + (g*.686) + (b*.168))
        newb = int((r*.272) + (g*.534) + (b*.131))
        return(newr,newg,newb)

    choice = '''
    Enter your choice :
    1 red
    2 darkpink
    3 skyblue
    4 lemonyellow
    5 grey
    6 sepia
    '''
    flag=0


    print(choice)

    n=input('Choice: ')
    try:
        no = int(n)
    except ValueError:
        print('Invalid input given. Try again! \nEnter a number between 1-6.')
        flag=2
    if no==None and flag==0:
                no=0
                print('Invalid input given. Try again! \nEnter a number between 1-6.')
                flag=1
    elif (no<1 or no>6) and flag==0:
                print('Invalid number given. Try again! \nEnter a number between 1-6.')
                flag=1
    elif flag==0:

        for py in range(height):
            for px in range(width):
                r,g,b = img.getpixel((px,py))
                if no==1:
                    pixels[px,py] = red(r,g,b)
                if no==2:
                    pixels[px,py] = darkpink(r,g,b)
                if no==3:
                    pixels[px,py] = skyblue(r,g,b)
                if no==4:
                    pixels[px,py] = lemongreen(r,g,b)
                if no==5:
                    pixels[px,py] = grey(r,g,b)
                if no==6:
                    pixels[px,py] = sepia(r,g,b)
        img.show()
    return img


#2-Gray Scaling
def grayscale(img):
    input_image = imread(img)
    inputimage = (input_image * 255).astype(np.uint8)
    pil_image = Image.fromarray(inputimage)
    pil_image.show()
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
    return grayscale_image



#3-Image Reconstruction

def reconstruction(img):
    img = Image.open(img)
    img = np.mean(img,2)

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

    m=100
    for i in range(0, m):
        S[i,i] = s[i]

    recon_img = U @ S @ V

    fig, ax = plt.subplots(1, 2)

    ax[0].imshow(img)
    ax[0].axis('off')
    ax[0].set_title('Original')

    ax[1].imshow(recon_img)
    ax[1].axis('off')
    ax[1].set_title(f'Reconstructed n = {m}')  

    plt.show()
    return recon_img



#4-Image Cropping
def crop(path):
    
    img = cv2.imread(path)

    print(img.shape) # Print image shape

    cv2.imshow("original", img)

    # Cropping an image

    cropped_image = img[80:280, 150:330]

    # Display cropped image

    cv2.imshow("cropped", cropped_image)

    
    cv2.waitKey(0)

    cv2.destroyAllWindows()
    return cropped_image




#5-Linear Filter
def linearfilter(path):
    window_name = 'filter2D Demo'
    img = path

    src = cv2.imread(cv2.samples.findFile(img), cv2.IMREAD_COLOR)
    if src is None:
        print('Error opening image!')
        print('Usage: filter2D.py [image_name -- default lena.jpg] \n')
        return -1
    
    ddepth = -1
    ind = 0
    round_counter = 0  # Counter to keep track of rounds
    display_time = 2000  # Display time in milliseconds (3 seconds)
    delay_time = 70  # Delay time for displaying image (medium speed)

    start_time = cv2.getTickCount()

    cv2.namedWindow(window_name)

    while True:
        kernel_size = 3 + 2 * (ind % 5)
        kernel = np.ones((kernel_size, kernel_size), dtype=np.float32)
        kernel /= (kernel_size * kernel_size)
        
        dst = cv2.filter2D(src, ddepth, kernel)
        
        cv2.imshow(window_name, dst)
        c = cv2.waitKey(delay_time)
        elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency() * 1000  # Calculate elapsed time in milliseconds

        if elapsed_time >= display_time:  # Stop and close window after 3 seconds
            break

        if ind == 10:
            round_counter += 1  # Increment round counter after 10 iterations
            #ind = 0  # Reset iteration counter for the next round
        ind += 1

    cv2.destroyAllWindows()
    return dst



#6-Image Resizing
def resize(path):
    img = cv2.imread(path)

    # displaying the image using imshow() function of cv2
    # In this : 1st argument is name of the frame
    # 2nd argument is the image matrix
    cv2.imshow('original image',img)

    # print shape of the image matrix
    # using shape attribute
    print("original image shape:",img.shape)

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

    cv2.imshow('resize image',resize_img)

    print("resize image shape:",resize_img.shape)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return resize_img



#7-Image Rotation
def rotation(path):
            image = cv2.imread(path)
            cv2.imshow("img",image)
            v1=180
            v2=90
            v3=40
            rotated_image1 = naive_image_rotate(image,v1,'full')
            rotated_image2 = naive_image_rotate(image,v2,'full')
            rotated_image3 = naive_image_rotate(image,v3,'full')
            '''cv2.imshow("original image", image)
            cv2.imshow("rotated_image1",rotated_image1)
            cv2.imshow("rotated_image2",rotated_image2)
            cv2.imshow("rotated_image3",rotated_image3)
            cv2.waitKey(0)
            cv2.destroyAllWindows()'''

            fig, axes = plt.subplots(1, 4, figsize=(12, 4))
            # Disable axis
            for ax in axes:
                ax.axis('off')

            # Plot original image
            axes[0].imshow(image)
            axes[0].set_title('Original Image')

            # Plot 
            axes[1].imshow(rotated_image1)
            axes[1].set_title('Rotation via 180 deg')

            # Plot 
            axes[2].imshow(rotated_image2)
            axes[2].set_title('Rotation via 90 deg')


            # Plot 
            axes[3].imshow(rotated_image3)
            axes[3].set_title('Rotation via 40 deg')

            # Adjust the layout to prevent overlapping
            plt.tight_layout()

            # Show the plot
            plt.show()

            titles=['Original Image','Rotation via 180 deg','Rotation via 90 deg', 'Rotation via 40 deg']
            l=[image,rotated_image1,rotated_image2,rotated_image3]

            #concatenated_image = cv2.hconcat([rotated_image1, rotated_image2, rotated_image3])
            return [axes, titles,l]

def naive_image_rotate(image, degrees, option='same'):

    # First we will convert the degrees into radians
    rads = math.radians(degrees)
    # Finding the center point of the original image
    cx, cy = (image.shape[1]//2, image.shape[0]//2)
    
    if(option!='same'):
        # Let us find the height and width of the rotated image
        height_rot_img = round(abs(image.shape[0]*math.sin(rads))) + \
                           round(abs(image.shape[1]*math.cos(rads)))
        width_rot_img = round(abs(image.shape[1]*math.cos(rads))) + \
                           round(abs(image.shape[0]*math.sin(rads)))
        rot_img = np.uint8(np.zeros((height_rot_img,width_rot_img,image.shape[2])))
        # Finding the center point of rotated image.
        midx,midy = (width_rot_img//2, height_rot_img//2)
    else:
        rot_img = np.uint8(np.zeros(image.shape))
     
    for i in range(rot_img.shape[0]):
        for j in range(rot_img.shape[1]):
            if(option!='same'):
                x= (i-midx)*math.cos(rads)+(j-midy)*math.sin(rads)
                y= -(i-midx)*math.sin(rads)+(j-midy)*math.cos(rads)
                x=round(x)+cy
                y=round(y)+cx
            else:
                x= (i-cx)*math.cos(rads)+(j-cy)*math.sin(rads)
                y= -(i-cx)*math.sin(rads)+(j-cy)*math.cos(rads)
                x=round(x)+cx
                y=round(y)+cy

            if (x>=0 and y>=0 and x<image.shape[0] and  y<image.shape[1]):
                rot_img[i,j,:] = image[x,y,:]
    return rot_img



#8-gaussian Filter
def gauss_fil(path):
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
        plt.show()
        return [axes,titles,l]
        

    def gaussian_filter(path):
                image = cv2.imread(path)
                gaussian_blur(image, 5, verbose=False)
                im=show(l,v)
                return im

    def convolution(image, kernel, average=False, verbose=False):
        if len(image.shape) == 3:
            print("\nFound 3 Channels : {}".format(image.shape))
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            print("Converted to Gray Channel. Size : {}".format(image.shape))
        else:
            print("Image Shape : {}".format(image.shape))
    
        print("Kernel Shape : {}".format(kernel.shape))

        plt.imshow(image, cmap='gray')
        plt.title("Image")
        plt.show()

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
    im=gaussian_filter(path)
    return im

#9-Median Filter
def median_filter(path):
    img = cv2.imread(path)

    #using medinaBlur() function to remove the noise from the given image

    median = cv2.medianBlur(img, 5)

    compare = np.concatenate((img, median), axis=1) 

    #displaying the noiseless image as the output on the screen

    #side by side comparison

    cv2.imshow('Median Filter', compare)

    cv2.waitKey(0)

    cv2.destroyAllWindows
    return median



#10-Image Scaling
def scaling(path):
        # Read image from disk.
        img = cv2.imread(path)
    
        # Get number of pixel horizontally and vertically.

        (height, width) = img.shape[:2]
    
        # Specify the size of image along with interploation methods.

        # cv2.INTER_AREA is used for shrinking, whereas cv2.INTER_CUBIC

        # is used for zooming.

        res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation = cv2.INTER_CUBIC)
    
        # Write image back to disk.
        cv2.imwrite('../Images/10_result.jpg', res)

        

        #showing the images
        cv2.imshow('original image',img)
        cv2.imshow('scaled image',res)   
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return res
      

#11-Image shearing
def shearing(path):
	# read the input image
    img = cv2.imread(path)
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
    return sheared_img


def select_image():
    print("\nSELECT YOUR IMAGE")
    print("a) 1_2_rover.jpg")           
    print("b) 3_4_turtle.jpg")
    print("c) 5_desktop.jpg ")      
    print("d) 6_scenary.jpg ")       
    print("e) 7_8_emoji.png")
    print("f) 9_person.png")
    print("g) 10_pig.jpg ")
    print("h) 11_apple.jpg ")
    print("i) IMG-IMPACT.png")

    choice=input("\nENTER SELECTION (case-sensitive): ")

    if choice=='a':
            p="1_2_rover.jpg"
    elif choice=='b':
            p="3_4_turtle.jpg"
    elif choice=='c':
            p="5_desktop.jpg"
    elif choice=='d':
            p="6_scenary.jpg"
    elif choice=='e':
            p="7_8_emoji.png"
    elif choice=='f':
            p="9_person.png"
    elif choice=='g':
            p="10_pig.jpg"
    elif choice=='h':
            p="11_apple.jpg"

    elif choice=='i':
            p="IMG-IMPACT.png"
    else:
            print('Invalid Selection! Default image selected...')
            p="IMG-IMPACT.png"

    path='../Images/'+p
    return path

def save_img(img,val,v):
    c=input('\nDo you want to save the filtered or editted image?\nEnter: \n 1 - for yes \n 0 - for no\nSELECTION: ')
    v=str(v)

    if c=='1':
            
            print("\nDefault name of new image is: ",v,"_fnew_editted.jpg' , if no input given. \n")
            print("Enter name of new Image : ",v,"_fnew_")
            in_n=input('')
            s="../Images/"+v+"_fnew_"+in_n+".jpg"
            if s=="../Images/"+v+"_fnew_.jpg":
                    s='../Images/'+v+'_fnew_editted.jpg'
            q=v+"_fnew_"+in_n+".jpg"
            if q==v+"_fnew_.jpg":
                q=v+'_fnew_editted.jpg'

            if val==1:
                img.save(s)
            elif val==2:
                plt.imsave(s, img, cmap='gray')
            elif val==3:
                plt.imsave(s, img)
            elif val==4:
                cv2.imwrite(s, img)
            elif val==5:
                axes=img[0]
                titles=img[1]
                l=img[2]
                fig, axes = plt.subplots(1, len(l), figsize=(15, 5))

                for i, img in enumerate(l):
                    axes[i].imshow(img, cmap='gray')
                    axes[i].set_title(titles[i])
                    axes[i].axis('off')
                plt.tight_layout()
                plt.savefig(s)
                           
            print('Filtered image saved as: ',q)

    elif c=='0':
        print('\nYou have selected not save the previous image.')

    else:
        print('\nInvalid Selection...Try Again.')
    


if __name__=='__main__':
    while True:
        print("\n\nMenu Driven Program")
        print("1.Colour Filter") 
        print("2.Gray Scaling") 
        print("3.Image Reconstruction") 
        print("4.Image Cropping") 
        print("5.Linear Filter") 
        print("6.Image Resizing") 
        print("7.Image Rotation")   
        print("8.Gaussian Filter") 
        print("9.Median Filter") 
        print("10.Image Scaling") 
        print("11.Image Shearing")
        print("12.Exit")
        choice=int(input("\nENTER YOUR CHOICE: "))
        if choice==1:
            p=select_image()
            print("\nCOLOUR FILTER\n")
            i=colorfilter(p)
            save_img(i,1,1)
        elif choice==2:
            p=select_image()
            print("\nGRAY SCALING\n") 
            i=grayscale(p)
            save_img(i,2,2)
        elif choice==3:
            p=select_image()
            print("\nIMAGE RECONSTRUCTION\n") 
            i=reconstruction(p)
            save_img(i,3,3)
        elif choice==4:
            p=select_image()
            print("\nIMAGE CROPPING\n") 
            i=crop(p)
            save_img(i,4,4)
        elif choice==5:
            p=select_image()
            print("\nLINEAR FILTER\n") 
            i=linearfilter(p)
            save_img(i,4,5)
        elif choice==6:
            p=select_image()
            print("\nIMAGE RESIZING\n") 
            i=resize(p)
            save_img(i,4,6)
        elif choice==7:
            p=select_image()
            print("\nIMAGE ROTATION\n")
            i=rotation(p)
            save_img(i,5,7)
        elif choice==8:
            p=select_image()
            print("\nGAUSSIAN FILTER\n") 
            i=gauss_fil(p)
            
            save_img(i,5,8)
        elif choice==9:
            p=select_image()
            print("\nMEDIAN FILTER\n") 
            i=median_filter(p)
            save_img(i,4,9)
        elif choice==10:
            p=select_image()
            print("\nIMAGE SCALING\n") 
            i=scaling(p)
            save_img(i,4,10)
        elif choice==11:
            p=select_image()
            print("\nIMAGE SHEARING\n")
            i=shearing(p)
            save_img(i,3,11)
        elif choice==12:
            print("\nEXITING APPLICATION!\n")
            break
        else:
            print("Invalid Choice! Try again...")
