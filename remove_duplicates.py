"""
This script remove duplicates images
from a directoryectory.
"""

#pip3 install pillow

import os, shutil, sys
from PIL import Image, ImageChops

def comparison(img1, img2):
    """
    Return the difference between to images
    """
    return ImageChops.difference(img1, img2)

def get_dim(img):
    """
    Return the size of an image
    """
    return img.size

def main():
    """
    Main function to manage the script
    """
    images = os.listdir('./input') #load images from input directory
    directory = os.getcwd()
    if not len(images):
        print('No images found')
        sys.exit(1)
    list_images = [Image.open(f'{directory}\\input\\{adresa}') for adresa in images] #get full path
    #####compare images and rename same images with same name
    for i in range(len(images) - 1):
        for j in range(i + 1, len(images)):
            if get_dim(list_images[i]) == get_dim(list_images[j]):
                diff = comparison(list_images[i], list_images[j]) 
                if not diff.getbbox(): 
                    images[i] = images[j]
    ########################
    images = set(images) #remove name duplicates from list of images
    for image in images:
        shutil.copy(f'{directory}\\input\\{image}',
                    f'{directory}\\output\\{image}') #copy the new list in ouput folder

if __name__ == "__main__":
    main()