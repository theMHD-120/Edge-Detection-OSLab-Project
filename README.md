# Edge-Detection-OSLab-Project
>>> Operating Systems Laboratiry final project - Summer 2024

# Project summary
||| In the name of ALLAH ||| <br />
----------------------------- <br />
Implementation of an Image Processing and a multithreading project: Edge Detection using Python's OpenCV library (to load, process and save the images). <br />
Before continuee, Please read the goal, instructions and the concept of this project from Assignment file ... <br />

## Used methods
As you saw, the main goal of this project is to create an edged image using the optimal and best multithreading method (for sub-matrices multiplications). For this approach, I used 3 methods for multithreading (fully and partial) which are:
- 1
- 2
- 3

## Results
Test both fully and partial multithreading methods (for different pictures) and see the results:
- Total taken time
- Obtained edged image

# About images
- Each image has n * m pixels:
  - n: rows
  - m: columns 

- image matrix = [ <br />
  [[R00, G00, B00], [R01, G01, B01], [R02, G02, B02], ..., [R0m, G0m, B0m]], <br />
  [[R10, G10, B10], [R11, G11, B11], [R12, G12, B12], ..., [R1m, G1m, B1m]], <br />
  [[R20, G20, B20], [R21, G21, B21], [R22, G22, B22], ..., [R2m, G2m, B2m]], <br />
  [[R30, G30, B30], [R31, G31, B31], [R32, G32, B32], ..., [R3m, G3m, B3m]], <br />
  [[R40, G40, B40], [R41, G41, B41], [R42, G42, B42], ..., [R4m, G4m, B4m]], <br />
  [[R50, G50, B50], [R51, G51, B01], [R52, G52, B52], ..., [R5m, G5m, B5m]], <br />
  ... <br />
  [[Rn0, Gn0, Bn0], [Rn1, Gn1, Bn1], [Rn2, Gn2, Bn2], ..., [Rnm, Gnm, Bnm]] <br />
  ] <br />
