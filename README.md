<a name="readme-top"></a>
# Image-Processing--IMG-IMPACT

In the project ```IMG-IMPACT``` several    ```Image Processing Techniques``` are used.



<details>
  <summary style="color: red;">Table of Contents</summary>
<li> <a href="#a1">Introduction</a></li>
<li> <a href="#a2"> Prerequisites and Techstack</a></li>
<li> <a href="#a3"> Steps for Execution </a></li>
<li>  <a href="#a4">Usage</a></li>
<a href="#end"><u><i>Skip to END...</i></u></a>
</details>
</br>

<a name="a1"></a>
## Introduction
```IMG-IMPACT``` is a project on <i> **Impacting the Images** </i>, using various ```Image Processing Technologies and Techniques``` .

These ```Techniques``` include various <i> **Filters** </i> like ```Median filter```, ```Gaussian filter```, ```Linear filter```, etc... 

The other ```Technologies``` implemented here are ```Scaling```, ```Cropping```, ```R0otation```, etc... 

</br>


### <b>Files :</b>

  In the ```IMG-IMPACT Directory``` there are 4 directories:
  
  - 1- ```Images Directory```- contains all the Images used in the programs.
    
  - 2- ```Individual_Filters&Techniques Directory```- contains the techniques and filters implemented separately.
    
  - 3- ```All_Filters_Combined Directory```- contains one program for the techniques and filters combined.
    
  - 4- ```Extra_Contents Directory```- contains extra information about the techniques and filters used.

</br>

### <b>Repository Structure :</b>

<details>
  <summary color= blue ><u> <b><i>IMG-IMPACT repo structure</i></b></u></summary>

  Below is the structure of the ```IMG-IMPACT``` project repository
  
  ```plaintext
    Image-Processing--IMG-IMPACT/
    │   
    ├── IMG-IMPACT/           # Project Folder
    │   │              
    │   ├── All_Filters_Combined/              # Folder3
    │   │    ├── IMG-IMPACT.py
    │   │    └── IMG-IMPACT.png    #logo
    │   │ 
    │   ├── Extra_Contents/                    # Folder4
    │   │    ├── IMG-IMPACT_Slides.pdf
    │   │    ├── IMG-IMPACT_Information.pdf
    │   │    └── IMG-IMPACT.png    #logo
    │   │ 
    │   ├── Images/                            # Folder1
    │   │    ├── 1_2_rover.jpg
    │   │    ├── 1_new_filtering.jpg
    │   │    ├── 3_4_turtle.jpg
    │   │    ├── 4_CroppedImage.jpg
    │   │    ├── 5_desktop.jpg
    │   │    ├── 6_scenary.jpg
    │   │    ├── 6_scenary1.jpg
    │   │    ├── 7_8_emoji.png.png
    │   │    ├── 9_person.png
    │   │    ├── 10_pig.jpg
    │   │    ├── 10_result.jpg
    │   │    └── IMG-IMPACT.png    #logo
    │   │ 
    │   ├── Individual_Filters&Techniques/     # Folder2
    │   │    ├── 1_ColourFilter.py
    │   │    ├── 2_GrayScale.py
    │   │    ├── 3_ImageReconstruction.py
    │   │    ├── 4_ImageCropping.py
    │   │    ├── 5_LinearFilter.py
    │   │    ├── 6_ImageResizing.py
    │   │    ├── 7.py
    │   │    ├── 8.py
    │   │    ├── 9_MedianFilter.py
    │   │    ├── 10_ImageScaling.py
    │   │    └── IMG-IMPACT.png   #logo
    │   │ 
    │   └── IMG-IMPACT.png   # Project Logo
    │   
    └─── README.md           # Repository README
    
  ```

</details>
</br>



### <b>Features :</b>

  - In **IMG-IMPACT** project ***Image Processing*** techniques are implemented.
      
  - Image processing involves ***manipulating images*** at a time and extracting useful insights from them.
      
  - Image can be represented as a ***grid of n x n small pieces***, which are called *pixels*.
      
  - If we can **assign numbers** to each colour, then, the grid of pixels can be represented as a ***numerical matrix***.
 ###
###

###
###

  <p align="right"><a href="#readme-top">Back to TOP</a></p>
  </br>

<!--
## Objective
* To transform an image to implement techniques, like image rotation, cropping, image smoothening, filters etc
* The techniques mentioned above are implemented using concepts such as linear transformation and SVD
###
###
  -->

  
<a name="a2"></a>
## Prerequisites and Techstack

<br>
    
  * Language :

    **Python**

<br>

  * Libraries :

    
    * OpenCV or cv2
    * Pillow or PIL
    * NumPy
    * argparse
    * matplotlib
    * math


<br>

  * Concepts :
    <details>
    <summary color= blue ><u> <b><i>Linear transformation, SVD, Fourier transformations</i></b></u></summary>

    
      * **Linear transformation** -

        Linear transformations are mathematical operations that maintain the fundamental properties of vector spaces.
        They are often represented using matrices and are essential in geometry, and transformations in computer graphics.
        They provide a structured way to describe and manipulate complex relationships between vectors.
        
      * **SVD**-
   
        Singular Value Decomposition, or SVD, is a powerful matrix factorization technique that breaks down a matrix into three simpler components: U, Σ, and V.
        Here, U and V are orthogonal matrices, and Σ is a diagonal matrix containing singular values.
        SVD is employed in image compression, as it uncovers hidden patterns and relationships in data
        
      * **Fourier transformations** -
   
        Fourier transformations are mathematical methods used to represent functions or signals in the frequency domain.
        The Fourier transform allows us to express complex signals as combinations of simpler sinusoidal components, revealing their frequency and amplitude characteristics.
        This is particularly useful for analyzing and processing signals in fields of image analysis, and data compression.

  </details>

  <p align="right"><a href="#readme-top">Back to TOP</a></p>
  </br>
  
  

<a name="a3"></a> 
## Steps for Execution

<br>

  1. Clone the ```'Image-Processing--IMG-IMPACT'``` github repository.
     ```sh
     git clone https://github.com/ankitacoder3/Image-Processing--IMG-IMPACT.git
      ```
     <br>
     
 2. Navigate to the ```'IMG-IMPACT' Directory``` in that.
    ```sh
    cd Image-Processing--IMG-IMPACT
    cd IMG-IMPACT
    ```
<br>

  3. Navigate to the ```'Individual_Filters&Technique' Directory``` to execute techniques and filters ```separately```.

     By opening any file in python idle and running it.

     <br>
     
4. Navigate to the ```'All_Filters_Combined' Directory``` to execute the techniques and filters ```combined```.
  
   By opening any file in python idle and running it.

   <br>
   
 5. Navigate to the ```'Extra_Contents' Directory``` to find ```extra information``` about the filters and techniques.

    <br>
    
    Note- For some filters and techniques information may not be complete or it may not exist in the'Extra_Contents' Directory.
  
  
  
  <p align="right"><a href="#readme-top">Back to TOP</a></p>
  </br>
   </br>

<a name="a4"></a>
## Usage



* IMG-IMPACT application can ***transform the pictures***, given as input, into different variations of the same picture.

  
* IMG-IMPACT application has ***many filters*** like linear filter, median filter etc. The user can ***select any filter***.

  
* IMG-IMPACT application also has ***many operations and methods*** such as rotating, cropping the image, etc. The user can ***select any method***.

  
* IMG-IMPACT can be used to ***create new images***, from the old images.

  <p align="right"><a href="#readme-top">Back to TOP</a></p>
  </br>
<a name="end"></a>
Thank you for exploring the IMG-IMPACT project. Happy Image Filtering and Processing! 🍿🎬

