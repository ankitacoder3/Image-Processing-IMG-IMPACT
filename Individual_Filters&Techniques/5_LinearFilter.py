
import sys
import cv2 as cv
import numpy as np
def main():
    window_name = 'filter2D Demo'
    #img=input("Enter image file name:")
    
    img='Images/5_desktop.jpg'
    imageName = img if len(img) > 0 else '4.jpg'
    # Loads an image
    src = cv.imread(cv.samples.findFile(imageName), cv.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: filter2D.py [image_name -- default lena.jpg] \n')
        return -1
    
    ddepth = -1
    
    ind = 0
    while True:
        
        kernel_size = 3 + 2 * (ind % 5)
        kernel = np.ones((kernel_size, kernel_size), dtype=np.float32)
        kernel /= (kernel_size * kernel_size)
        
        dst = cv.filter2D(src, ddepth, kernel)
        
        cv.imshow(window_name, dst)
        c = cv.waitKey(1000)
        if ind == 10:
            break
        ind += 1
    return 0

main()
