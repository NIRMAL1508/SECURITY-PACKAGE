# Importing all the necessary libraries
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
import lorenzKey as key
from PIL import Image

def greyen(path,x,y,z):
    image = img.imread(path)

    height = image.shape[0]
    width = image.shape[1]

   
    keyx = float(x)
    keyy = float(y)
    keyz = float(z)
    x, y, keys = key.lorenz_key(keyx, keyy, keyz, height*width)
    l = 0

    encrypted = np.zeros(shape=[height, width, 3], dtype=np.uint8)
    # print(keys)
    for i in range(height):
        for j in range(width):
        
            zk = (int((keys[l]*pow(10, 5))%256))
            
            encrypted[i, j] = image[i, j]^zk
            l += 1

    enimg=Image.fromarray(encrypted)
    enimg.save("encrypted.jpg")

def greyde(path,x,y,z):
   
    encrypted = img.imread(path)
    height = encrypted.shape[0]
    width = encrypted.shape[1]
    keyx = float(x)
    keyy = float(y)
    keyz = float(z)
    x, y, keys = key.lorenz_key(keyx, keyy, keyz, height*width)
    decrypted = np.zeros(shape=[height, width, 3], dtype=np.uint8)
    l = 0
    for i in range(height):
        for j in range(width):
            zk = (int((keys[l]*pow(10, 5))%256))
            decrypted[i, j] = encrypted[i, j]^zk
           
            l += 1


    deimg=Image.fromarray(decrypted)
    deimg.save("decrypted.jpg")

