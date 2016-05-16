import matplotlib.image as mpimg

import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

n_colors = 8

def read_image(file_path):
    original_image = mpimg.imread(file_path) # return arr

    print('3D array --- ')
    print(original_image)

    # convert integer array image to float image
    image = np.array(original_image, dtype = np.float64) / 255

    # load image and transform to 2d image
    w, h, d = original_shape = tuple(image.shape)
    assert  d == 3

    print('w - h - d: ')
    print(w, h, d)

    array_image = np.reshape(image, (w * h, d))

    print('2D array --- ')
    print(array_image)

    kModel = KMeans(n_clusters = n_colors)
    kModel.fit(array_image)

    kLabels = kModel.predict(array_image)

    print('KLabels --- ')
    print(kLabels)

    # Create new image
    # # empty image
    new_image = np.zeros((w, h, d))
    label_idx = 0

    for i in range(w):
        for j in range(h):
            new_image[i][j] = kModel.cluster_centers_[kLabels[label_idx]]
            label_idx += 1


    plt.figure(1)
    plt.clf()
    ax = plt.axes([0, 0, 1, 1])
    plt.title('Original image')
    plt.imshow(original_image)

    plt.figure(2)
    plt.clf()
    ax = plt.axes([0, 0, 1, 1])
    plt.title('2D image')
    plt.imshow(image)

    plt.figure(3)
    plt.clf()
    ax = plt.axes([0, 0, 1, 1])
    plt.title('Quantized Image by 8 colors')
    plt.imshow(new_image)

    plt.show()

read_image('../../data/halongbay.jpg')