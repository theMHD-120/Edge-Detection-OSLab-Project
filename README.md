# Edge-Detection-OSLab-Project
>>> Operating Systems Laboratiry final project - Summer 2024

# Project summary
||| In the name of ALLAH ||| <br />
----------------------------- <br />
Implementation of an Image Processing and a multithreading project: Edge Detection using Python's OpenCV library (to load, process and save the images). <br />
Before proceeding, please read the concept, purpose and instructions of this project from the Assignment file.

## Methods
As you saw, the main goal of this project is to create an edged image using the optimal and best multithreading method (for sub-matrices multiplications). For this approach, I used 3 methods for multithreading (fully and partial) which are:

- Partial Multithreading:
  - Using multithreading to calculate the each ROW of Gx and Gy matrices in parallel 
  - Less time spend, higher performance, lower memory usage and has the more optimal result

- Fully Multithreading (1D thread):
  - Using multithreading to calculate the each ELEMENT of Gx and Gy matrices in parallel
  - Compared with 2D: Less time spend, higher performance, lower memory usage and has the more optimal result
    
- Fully Multithreading (2D thread):
  - Using multithreading to calculate the each ELEMENT of each ROW of Gx and Gy matrices in parallel
  - Compared with 1D: More time spend, lower performance, higher memory usage and doesn't have the optimal result

## Results
Test both fully and partial multithreading methods (for different pictures) and see the results:
- Total taken time
- Obtained edged image

# Image file
Information of an image file and how does it considered as a matrix of some pixels. A pixel is one of the small dots or squares that make up an image on a computer screen. <BR />
In a RGB image, each color pixel is composed of three separate color components. These components can be represented as combinations of red, green and blue (RGB), or hue, saturation and intensity (HSI). For both RGB and HSI, each component of a pixel is converted to a value from 0 to 255.

- Each image with n * m pixels:
  - n: rows
  - m: columns
     
- Image matrix =
-       [ 
       [[R00, G00, B00], [R01, G01, B01], [R02, G02, B02], ..., [R0m, G0m, B0m]], <br />
       [[R10, G10, B10], [R11, G11, B11], [R12, G12, B12], ..., [R1m, G1m, B1m]], <br />
       [[R20, G20, B20], [R21, G21, B21], [R22, G22, B22], ..., [R2m, G2m, B2m]], <br />
       [[R30, G30, B30], [R31, G31, B31], [R32, G32, B32], ..., [R3m, G3m, B3m]], <br />
       [[R40, G40, B40], [R41, G41, B41], [R42, G42, B42], ..., [R4m, G4m, B4m]], <br />
       [[R50, G50, B50], [R51, G51, B01], [R52, G52, B52], ..., [R5m, G5m, B5m]], <br />
       ... <br />
       [[Rn0, Gn0, Bn0], [Rn1, Gn1, Bn1], [Rn2, Gn2, Bn2], ..., [Rnm, Gnm, Bnm]] <br />
      ] </pre>
