<a name="readme-top"></a>
# Image-Processing-IMG-IMPACT

In the project ```IMG-IMPACT```, several    ```Image Processing Techniques``` are used, to ````IMPACT THE IMAGES````.

This project is based on the ```Linear Algebra project```, which was part of the course ```UE20MA251```.

<br>

<details open>

  <summary style="color: red;">Table of Contents</summary>
<li> <a href="#a1">Introduction</a></li>
<li> <a href="#a2"> Prerequisites and Techstack</a></li>
<li> <a href="#a3"> Steps for Execution </a></li>
<li>  <a href="#a5">Screenshots</a></li>
<li>  <a href="#a4">Usage</a></li>
<a href="#end"><u><i>Skip to END...</i></u></a>
</details>
</br>

<a name="a1"></a>
## Introduction
```IMG-IMPACT``` is a project on <i> **Impacting the Images** </i>, using various ```Image Processing Technologies and Techniques``` .

These ```Techniques``` include various <i> **Filters** </i> like ```Median filter```, ```Gaussian filter```, ```Linear filter```, etc... 

The other ```Technologies``` implemented here are ```Scaling```, ```Cropping```, ```Rotation```, etc... 

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
  <summary color= blue ><u><b><i>IMG-IMPACT repo structure</i></b> click...</u></summary>

  Below is the structure of the ```IMG-IMPACT``` project repository
  
  ```plaintext
    Image-Processing-IMG-IMPACT/
    │   
    ├── IMG-IMPACT/           # Project Folder
    │   │              
    │   ├── All_Filters_Combined/              # Folder3
    │   │    └── IMG-IMPACT.py
    │   │     
    │   ├── Extra_Contents/                    # Folder4
    │   │    ├── IMG-IMPACT_Slides.pdf
    │   │    └── IMG-IMPACT_Information.pdf
    │   │ 
    │   ├── Images/                            # Folder1
    │   │    ├── 1_2_rover.jpg
    │   │    ├── 3_4_turtle.jpg
    │   │    ├── 4_CroppedImage.jpg
    │   │    ├── 5_desktop.jpg
    │   │    ├── 6_scenary.jpg
    │   │    ├── 7_8_emoji.png
    │   │    ├── 9_person.png
    │   │    ├── 10_pig.jpg
    │   │    ├── 11_apple.jpg
    │   │    ├── <no.>_new_<any name>.jpg      
    │   │          # These files are the resultant images after running the files, present in the 'Individual_Filters_Techniques' Folder.
    │   │    ├── <no.>_fnew_<any name>.jpg      
    │   │          # These files are the resultant images after running the file, present in the 'All_Filters_Combined' Folder.
    │   │    └── IMG-IMPACT.png    #logo
    │   │ 
    │   ├── Individual_Filters_Techniques/     # Folder2
    │   │    ├── 1_ColourFilter.py
    │   │    ├── 2_GrayScale.py
    │   │    ├── 3_ImageReconstruction.py
    │   │    ├── 4_ImageCropping.py
    │   │    ├── 5_LinearFilter.py
    │   │    ├── 6_ImageResizing.py
    │   │    ├── 7_ImageRotation.py
    │   │    ├── 8_GaussianFilter.py
    │   │    ├── 9_MedianFilter.py
    │   │    ├── 10_ImageScaling.py
    │   │    └── 11_ImageShearing.py
    │   │ 
    │   └── IMG-IMPACT.png   # Project Logo
    │   
    └─── README.md           # Repository README
    
  ```

</details>
</br>



### <b>Underlying concepts / theory :</b>

  1.  **Inclusion of Image Processing Techniques**
     
      The project ```IMG-IMPACT``` involves the implementation of ```Image Processing Techniques```.

  2.  **Manipulation of Images and Extraction of Insights**

      Image processing entails the ```manipulation of images```to extract ```useful insights``` from them.

  3.  **Representation of Images as Grids of Pixels**

      Images can be represented as a ```grid of n x n small pieces```, which are called ```pixels```.

  4.  **Numerical Representation of Image Pixels**
 
      If we can ```assign numbers to each colour```, then, the grid of pixels can be represented as a ```numerical matrix```.
    
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
    <summary color= blue><u><b><i style="color: blue;">Linear transformation, SVD, Fourier transformations</i></b> (click for more details...)</u></summary>
      
    <p style="fontcolor: purple;">
      
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

</p>
  </details>

  <p align="right"><a href="#readme-top">Back to TOP</a></p>
  </br>
  
  

<a name="a3"></a> 
## Steps for Execution

<br>

  1. Clone the ```'Image-Processing-IMG-IMPACT'``` github repository.
     ```sh
     git clone https://github.com/ankitacoder3/Image-Processing-IMG-IMPACT.git
      ```
     <br>
     
 2. Navigate to the ```'IMG-IMPACT' Directory``` in that.
    ```sh
    cd Image-Processing--IMG-IMPACT
    cd IMG-IMPACT
    ```
  <br>

  3. Navigate to ```ANY of the Directories``` and ```execute the respective files``` present in that directory.



      <br>

     
      i.  ***Navigation*** :
          <br><br>
           a. Navigate to  ```'Individual_Filters_Techniques' Directory``` to execute techniques and filters ```separately```.
        ```sh
        cd Individual_Filters_Techniques
        ```
      
      <br>

     b. Navigate to  ```'All_Filters_Combined' Directory``` to execute techniques and filters ```combined```.
      ```sh
      cd All_Filters_Combined
      ```
      
      <br>
      
      c. Navigate to  ```'Extra_Contents' Directory``` to find ```extra information``` about the filters and techniques.
      ```sh
      cd Extra_Contents
      ```
      
      <br>
           
     d. Navigate to  ```'Images' Directory``` to ```edit``` the images used.
      ```sh
      cd Images
      ```
      
       <p align="right"><a href="#readme-top">Back to TOP</a></p> <br>
      
     ii.  ***Execution*** :

     By opening ```any file``` in ```python idle``` or ```command prompt```, and running it.
     
     <br>
     
     a. To execute any file from command prompt, type
        ```sh
        python <filename>
        ```

        Then ```follow the instructions```, which appear on ```command prompt```.
      
      <br>

     b. For any file from  ```'Individual_Filters_Techniques' Directory```, say ```1_ColourFilter.py```, type
      ```sh
      python 1_ColourFilter.py
      ```

      Then ```follow the instructions```, which appear on ```command prompt```.
      
      <br>
      
      c. For any file from  ```'All_Filters_Combined' Directory```, say ```IMG-IMPACT.py```, type
      ```sh
      python IMG-IMPACT.py
      ```

      Then ```follow the instructions```, which appear on ```command prompt```.
      
      <br>
    
     

     <br>
    
  Note- For some filters and techniques information may not be complete or it may not exist in the'Extra_Contents' Directory.
  
  
  
  <p align="right"><a href="#readme-top">Back to TOP</a></p>
  </br>
   </br>

   <a name="a5"></a> 
## Screenshots

<br>


  * All images before and ***after using IMG-IMPACT***
    
  ![image](https://github.com/ankitacoder3/Image-Processing--IMG-IMPACT/assets/73939061/1f99828b-e6bb-4c3e-8260-37a794cfb734)


<br>


  * Select ***any filter or technique***  of your choice

  ![image](https://github.com/ankitacoder3/Image-Processing--IMG-IMPACT/assets/73939061/f0afd5ed-9aba-4be3-9232-d46eea54ac8d)

<br>
<p align="right"><a href="#readme-top">Back to TOP</a></p>

  * Select ***any image*** of your choice

  ![image](https://github.com/ankitacoder3/Image-Processing--IMG-IMPACT/assets/73939061/014f3e57-1455-4f71-85d9-f792d1992c17)

<br>

  * Choose if you ***want to save editted images*** or not

  ![image](https://github.com/ankitacoder3/Image-Processing--IMG-IMPACT/assets/73939061/d865cec1-ad34-4e31-99d5-f6e505e9e7eb)


<br>

  * Choose if you ***want to name the filtered images***

  ![image](https://github.com/ankitacoder3/Image-Processing--IMG-IMPACT/assets/73939061/c15ab7de-4d19-4b15-bbe6-299657546903)


  * & Much More...


  <p align="right"><a href="#readme-top">Back to TOP</a></p>
  </br>
   </br>

<a name="a4"></a>
## Usage

<br>

* IMG-IMPACT application can ***transform the pictures***, given as input, into ***different variations*** of the same picture.


* IMG-IMPACT application has ***many default images*** in the 'Images' directory. The user can ***select any image***.

  
* IMG-IMPACT application has ***many filters*** like linear filter, median filter etc. The user can ***select any filter***.

  
* IMG-IMPACT application also has ***many operations and methods*** such as rotating, cropping the image, etc. The user can ***select any method***.

  
* IMG-IMPACT can be used to ***create new images***, from the old images.

  
* Finally, IMG-IMPACT can be used to save the ***new  created, editted and filtered images***, with ***default image names or user defined names***, as per the ***user's choice***.

* This project could also be used as a `project` for `Linear Algebra courses`, like `UE20MA251` or ue20ma251.

      
* Other Examples or Other Usage:
    * Use IMG-IMPACT to batch process a series of images with a specific filter.
    * Employ IMG-IMPACT in a data preprocessing pipeline for machine learning models that require image data.
    * Utilize IMG-IMPACT for educational purposes to demonstrate the effects of different image processing techniques.

  <p align="right"><a href="#readme-top">Back to TOP</a></p>
  </br>
  
<a name="end"></a>
Thank you for exploring the IMG-IMPACT project. Happy Image Editting, Filtering and Processing! 🖼️ 🔄


###
