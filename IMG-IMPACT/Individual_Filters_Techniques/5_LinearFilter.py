import cv2 as cv
import numpy as np

def save_filtered_image(image, filename):
    if image is not None and image.any():
        print("\nDefault name of the new image is: '5_new_linearfilter.jpg', if no input given.\n")
        in_n = input("Enter name of the new Image: 5_new_")

        if in_n == "":
            s = "../Images/5_new_linearfilter.jpg"
            cv.imwrite(s, image)
            q = '5_new_linearfilter.jpg'
        else:
            s = "../Images/5_new_" + in_n + ".jpg"
            if s == "../Images/5_new_.jpg":
                s = '../Images/5_new_linearfilter.jpg'
            cv.imwrite(s, image)
            q = "5_new_" + in_n + ".jpg"

        if q == "5_new_.jpg":
            q = '5_new_linearfilter.jpg'
        print('Filtered image saved as:', q)

def main():
    window_name = 'filter2D Demo'
    img = '../Images/5_desktop.jpg'

    src = cv.imread(cv.samples.findFile(img), cv.IMREAD_COLOR)
    if src is None:
        print('Error opening image!')
        print('Usage: filter2D.py [image_name -- default lena.jpg] \n')
        return -1
    
    ddepth = -1
    ind = 0
    round_counter = 0  # Counter to keep track of rounds
    display_time = 2000  # Display time in milliseconds (3 seconds)
    delay_time = 70  # Delay time for displaying image (medium speed)

    start_time = cv.getTickCount()

    cv.namedWindow(window_name)

    while True:
        kernel_size = 3 + 2 * (ind % 5)
        kernel = np.ones((kernel_size, kernel_size), dtype=np.float32)
        kernel /= (kernel_size * kernel_size)
        
        dst = cv.filter2D(src, ddepth, kernel)
        
        cv.imshow(window_name, dst)
        c = cv.waitKey(delay_time)
        elapsed_time = (cv.getTickCount() - start_time) / cv.getTickFrequency() * 1000  # Calculate elapsed time in milliseconds

        if elapsed_time >= display_time:  # Stop and close window after 3 seconds
            break

        if ind == 10:
            round_counter += 1  # Increment round counter after 10 iterations
            #ind = 0  # Reset iteration counter for the next round
        ind += 1

    cv.destroyAllWindows()
    save_filtered_image(dst, img)

if __name__ == "__main__":
    main()
