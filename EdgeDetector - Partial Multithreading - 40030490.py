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
    >- Partial Multithreading:
    >>> Using multithreading to calculate the each ROW of Gx and Gy matrices in parallel 
    >>> Less time spend, higher performance, lower memory usage and has the more optimal result

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

# Calculate the Gx and Gy in a row for each 3*m matrix of an image  -------------------------
def row_calculation(row_index):
    sumX_list = []
    sumY_list = []
    
    for j in range(img_width - 2):
        sumX_DL = 0
        sumY_DL = 0
        
        # summation for Gx
        sumX_DL += (gray_matrix[row_index][j] * X_DL[0][0] + gray_matrix[row_index][j + 1] * X_DL[0][1] + gray_matrix[row_index][j + 2] * X_DL[0][2])
        sumX_DL += (gray_matrix[row_index + 1][j] * X_DL[1][0] + gray_matrix[row_index + 1][j + 1] * X_DL[1][1] + gray_matrix[row_index + 1][j + 2] * X_DL[1][2])
        sumX_DL += (gray_matrix[row_index + 2][j] * X_DL[2][0] + gray_matrix[row_index + 2][j + 1] * X_DL[2][1] + gray_matrix[row_index + 2][j + 2] * X_DL[2][2])
        sumX_list.append(sumX_DL)
        
        # summation for Gy
        sumY_DL += (gray_matrix[row_index][j] * Y_DL[0][0] + gray_matrix[row_index][j + 1] * Y_DL[0][1] + gray_matrix[row_index][j + 2] * Y_DL[0][2])
        sumY_DL += (gray_matrix[row_index + 1][j] * Y_DL[1][0] + gray_matrix[row_index + 1][j + 1] * Y_DL[1][1] + gray_matrix[row_index + 1][j + 2] * Y_DL[1][2])
        sumY_DL += (gray_matrix[row_index + 2][j] * Y_DL[2][0] + gray_matrix[row_index + 2][j + 1] * Y_DL[2][1] + gray_matrix[row_index + 2][j + 2] * Y_DL[2][2])
        sumY_list.append(sumY_DL)
        
    Gx.append(sumX_list)
    Gy.append(sumY_list)

# Calculate the Gx and Gy matrices in parallel (multithreading) -----------------------------
def G_calculaton():
    threads_list = []
    
    for i in range(img_height - 2):
        row_thread = th.Thread(target=row_calculation, args=(i,)) 
        row_thread.start()
        threads_list.append(row_thread)
        
    for thread in threads_list:
        thread.join()

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