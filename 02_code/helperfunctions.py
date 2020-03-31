import glob
import cv2
import numpy as np
from skimage.transform import resize
from skimage.io import imread
from sklearn.decomposition import PCA
import skimage
from sklearn.cluster import KMeans
from collections import Counter
import matplotlib.pyplot as plt



def add(a, b):
    """
    Crazy math stuff
    """
    return a + b

def load_images(paths, col=False):
    """
    Load all images from specified path
    """
    images = []
    if col == True:
        # Load images just the 30th of august - index 213
        image_files = sorted(glob.glob(paths[213] +"/*"))
        for ff in image_files:
                im = skimage.io.imread(ff, as_gray=False)
                images.append(im)        
    
    else:
        image_files = sorted(glob.glob(paths[0] +"/*"))
        for ff in image_files:
            im = skimage.io.imread(ff, as_gray=True)
            images.append(im)
    return images

def extract_dim(image_object):
    im = np.asarray(image_object)
    dim = np.asarray(im.shape).shape
    return dim[0]

def reshape_images(image1, image2):
    if extract_dim(image1) > 2:
        n = image1.shape[0]
        new_size = np.asarray(image1[0].shape) / 5
        new_size = new_size.astype(int) * 5
        new_size = [n, new_size[0], new_size[1]]
        im1 = resize(image1, new_size)
        im2 = resize(image2, new_size)
    else:
        new_size = np.asarray(image1.shape) / 5
        new_size = new_size.astype(int) * 5
        im1 = resize(image1, new_size)
        im2 = resize(image2, new_size)
    return im1, im2


def subtract_images(image1, image2):
    # Function for pixel by pixel subtraction
    im1 = np.asarray(image1)
    im2 = np.asarray(image2)
    
    im1, im2 = reshape_images(im1, im2)
    
    # Subtraction
    return np.abs(im1 - im2)

def subtract_c_images(image1, image2):
    # Function for pixel by pixel subtraction
    im1 = []
    im2 = []
    for i in range(len(image1)):
        img1 = cv2.cvtColor(image1[i], cv2.COLOR_RGB2GRAY)
        img2 = cv2.cvtColor(image2[i], cv2.COLOR_RGB2GRAY)
        im1.append(img1)
        im2.append(img2)
    im1 = np.asarray(im1)
    im2 = np.asarray(im2)
    
    im1, im2 = reshape_images(im1, im2)
    
    # Subtraction
    return np.abs(im1 - im2)

def find_vector_set(diff_image, new_size, h):
    
    i = 0
    j = 0
    vector_set = np.zeros((int(new_size[0] * new_size[1] / h**2), h**2))
    
    while i < vector_set.shape[0]:
        while j < new_size[0]:
            k = 0
            while k < new_size[1]:
                block = diff_image[j:j+h, k:k+h]
                feature = block.ravel()
                vector_set[i, :] = feature
                k += h
            j += h
        i += 1
    mean_vec = np.mean(vector_set, axis=0)
    #mean normalization
    vector_set = vector_set - mean_vec   
    return vector_set, mean_vec


def find_FVS(EVS, diff_image, mean_vec, new):
    i = 2
    feature_vector_set = []
    while i < new[0] - 2:
        j = 2
        while j < new[1] - 2:
            block = diff_image[i-2:i+3, j-2:j+3]
            feature = block.flatten()
            feature_vector_set.append(feature)
            j += 1
        i += 1
    FVS = np.dot(feature_vector_set, EVS)
    FVS = FVS - mean_vec
    return FVS



def clustering(FVS, components, new):
    kmeans = KMeans(components, verbose = 0)
    kmeans.fit(FVS)
    output = kmeans.predict(FVS)
    count  = Counter(output)
    least_index = min(count, key = count.get)
    #TODO Check why -4 in reshape function; original: np.reshape(output, (new[0] - 4, new[1] - 4))
    change_map  = np.reshape(output,(new[0], new[1]))
    return least_index, change_map