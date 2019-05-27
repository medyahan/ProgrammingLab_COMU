import matplotlib.pyplot as plt
import numpy as np

def my_rot(img):
    m = img.shape[0]
    n = img.shape[1]
    my_new_image = np.zeros((m, n, 3), dtype = int)

    for row in range(m):
        for col in range(n):
            my_new_image[col][row] = img[row][col]  # bunun kendisi de bir liste
            # my_new_image[col][row][:] = img[row][col][:]   bunlarin hepsi olur
            # my_new_image[col,row,:] = img[row,col,:]
    return my_new_image

def my_convert_rgb_to_gray(img):
    m = img.shape[0]
    n = img.shape[1]
    my_new_image = np.zeros((m, n), dtype = int)

    for row in range(m):
        for col in range(n):
            my_new_image[row, col] = my_norm(img[row, col, :])
    return my_new_image

def my_norm(my_v):
    return int(((my_v[0]**2)+(my_v[1]**2)+(my_v[2]**2))**0.5)

def my_norm_1(my_v):
    s= int(((my_v[0]**2)+(my_v[1]**2)+(my_v[2]**2))**0.5)
    if s > 280:
        return 1
    else:
        return 0

def my_convert_gray_to_bw(img):
    m = img.shape[0]
    n = img.shape[1]
    my_new_image = np.zeros((m, n), dtype = int)

    for row in range(m):
        for col in range(n):
            my_new_image[row, col] = my_norm_1(img[row, col, :])

    return my_new_image

file_name = "bird_1.jpg"
img1 = plt.imread(file_name)
img2 = my_rot(img)
img3 = my_convert_gray_to_bw(img2)
img4 = my_convert_rgb_to_gray(img2)

plt.subplot(1, 4, 1)
plt.imshow(img1)
plt.subplot(1, 4, 2)
plt.imshow(img2)
plt.subplot(1, 4, 3)
plt.imshow(img3, cmap = 'gray')
plt.subplot(1, 4, 4)
plt.imshow(img4, cmap = 'gray')

