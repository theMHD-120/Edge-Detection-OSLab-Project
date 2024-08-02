"""
    ||| In the name of ALLAH |||
    -----------------------------
    Seyed Mahdi Mahdavi Mortazavi 
    StdNo.: 40030490
    -----------------------------
    Operating Systems Laboratory
    Assignement: Final Project
    >- Image Processing: 
    >>> Edge Detector Filter
    >- Fully Multithreading (2D thread):
    >>> Using multithreading to calculate the each ELEMENT of each ROW of Gx and Gy matrices in parallel
    >>> Compared with 1D: More time spend, lower performance, higher memory usage and doesn't have the optimal result

"""
import re
import os
import time
import cv2 as cv
import numpy as np
import threading as th

# Global variables --------------------------------------------------------------------------
img_width = 0
img_height = 0
gray_matrix = []
img_matrices = []
edges_matrix = []
grayscale_matrix = []
Gx = [] # result of X-Direction Kernel
Gy = [] # result of Y-Direction Kernel
X_DL = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]] # X - Direction Kernel
Y_DL = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]] # Y - Direction Kernel

# Search for the pattern in the input (path) string -----------------------------------------
def get_image_name(path, pattern):
    match = re.search(pattern, path)
    return match.group(1)

# load the image ----------------------------------------------------------------------------
def load_image():
    global img_matrices, img_height, img_width
    img_matrices = cv.imread(path)
    img_height = len(img_matrices)
    img_width = len(img_matrices[0])

# Convert RGB to Gray color -----------------------------------------------------------------
def rgb_to_gray():
    for row in img_matrices:
        gray_row = []
        for rgb_array in row:
            gray_row.append(0.2989 * rgb_array[0]  +  0.5870 * rgb_array[1]   +  0.1140 * rgb_array[2])
        gray_matrix.append(gray_row)

# Calculate the elemnts of Gx and Gy rows for each 3*3 matrix of an image -------------------
def element_calculation(row_index, col_index, Gx_row, Gy_row):
    sumX_DL = 0
    sumY_DL = 0
    
    # summation for Gx row
    sumX_DL += (gray_matrix[row_index][col_index] * X_DL[0][0] + gray_matrix[row_index][col_index + 1] * X_DL[0][1] + gray_matrix[row_index][col_index + 2] * X_DL[0][2])
    sumX_DL += (gray_matrix[row_index + 1][col_index] * X_DL[1][0] + gray_matrix[row_index + 1][col_index + 1] * X_DL[1][1] + gray_matrix[row_index + 1][col_index + 2] * X_DL[1][2])
    sumX_DL += (gray_matrix[row_index + 2][col_index] * X_DL[2][0] + gray_matrix[row_index + 2][col_index + 1] * X_DL[2][1] + gray_matrix[row_index + 2][col_index + 2] * X_DL[2][2])
    Gx_row.append(sumX_DL)
    
    # summation for Gy row
    sumY_DL += (gray_matrix[row_index][col_index] * Y_DL[0][0] + gray_matrix[row_index][col_index + 1] * Y_DL[0][1] + gray_matrix[row_index][col_index + 2] * Y_DL[0][2])
    sumY_DL += (gray_matrix[row_index + 1][col_index] * Y_DL[1][0] + gray_matrix[row_index + 1][col_index + 1] * Y_DL[1][1] + gray_matrix[row_index + 1][col_index + 2] * Y_DL[1][2])
    sumY_DL += (gray_matrix[row_index + 2][col_index] * Y_DL[2][0] + gray_matrix[row_index + 2][col_index + 1] * Y_DL[2][1] + gray_matrix[row_index + 2][col_index + 2] * Y_DL[2][2])
    Gy_row.append(sumY_DL)

# Calculate the rows of Gx and Gy in parallel (multithreading) ------------------------------
def row_calculation(row_index):
    Gx_row = []
    Gy_row = []
    elementsthreads_list = []
    
    for j in range(img_width - 2):
        element_thread = th.Thread(target=element_calculation, args=(row_index, j, Gx_row, Gy_row,)) 
        element_thread.start()
        elementsthreads_list.append(element_thread)
        
    for elementthread in elementsthreads_list:
        elementthread.join()
        
    Gx.append(Gx_row)
    Gy.append(Gy_row)

# Calculate the Gx and Gy matrices in parallel (multithreading) -----------------------------
def G_calculaton():
    rowthreads_list = []
    
    for i in range(img_height - 2):
        row_thread = th.Thread(target=row_calculation, args=(i,)) 
        row_thread.start()
        rowthreads_list.append(row_thread)
        
    for rowthread in rowthreads_list:
        rowthread.join()

# Convert to the Grayscale matrix -----------------------------------------------------------
def gray_to_grayscale():
    global grayscale_matrix
    
    for i in range(img_height - 2):
        grayscale_row = []
        for j in range(img_width - 2):
            grayscale_row.append(np.floor(np.sqrt(np.power(Gx[i][j], 2) + np.power(Gy[i][j], 2))))
        grayscale_matrix.append(np.array(grayscale_row))
        
    grayscale_matrix = np.array(grayscale_matrix)

# Apply the edge detection ------------------------------------------------------------------
def grayscale_to_edges():
    global edges_matrix
    threshold = np.mean(grayscale_matrix) # mean of all values in grayscale_matrix
    
    for row in grayscale_matrix:
        edge_row = []
        for value in row:
            if value <= threshold:
                edge_row.append(255)
            else:
                edge_row.append(0)
        edges_matrix.append(np.array(edge_row))
        
    edges_matrix = np.array(edges_matrix)

# Print the matrices ------------------------------------------------------------------------
def print_results():
    os.system('cls')
    print("1) Image matrix:")
    print(img_matrices)

    print("\n2) Grayscale matrix:")
    print(grayscale_matrix)

    print("\n3) Edge Detection matrix:")
    print(edges_matrix)

# Save the edge detection result to the new path --------------------------------------------
def save_result(image_name):
    # See the result image (edges matrix) from this new path
    cv.imwrite(f"./Edges/{image_name} - Edges.png", edges_matrix)

# Main part with function calls -------------------------------------------------------------
if __name__ == '__main__':
    t1 = time.time()
    
    # Image path and necessary pattern
    path = "./Main images/MyPicture1.png"
    pattern = r"\/([A-Za-z0-9]+)\.(png|jpg)$"
    image_name = get_image_name(path, pattern)
    
    # Load the image matrices 
    load_image()
    
    # Convert the image matrix to gray
    rgb_to_gray()
    
    # Convert the gray matrix to grayscale
    G_calculaton()
    gray_to_grayscale()
    
    # Convert the grayscale matrix to edges
    grayscale_to_edges()
    
    # Print the image, grayscale and edges matrix
    print_results()
    
    # Save the edge matrix (edge image)
    save_result(image_name) 
    
    # The total taken time
    t2 = time.time()
    print(f"\n>>> Time taken: {t2 - t1} seconds")