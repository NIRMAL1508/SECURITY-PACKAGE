import LogisticKey as key   
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image

def logisticen(path,x,y):
    image = img.imread(path)


    height = image.shape[0]
    width = image.shape[1]
    

    generatedKey = key.logistic_key(x, y, height*width) 
    

    z = 0

    encryptedImage = np.zeros(shape=[height, width, 3], dtype=np.uint8)

    for i in range(height):
        for j in range(width):

            encryptedImage[i, j] = image[i, j].astype(int) ^ generatedKey[z]
            z += 1

   
    enimg = Image.fromarray(encryptedImage)
    enimg.save("encryptedImage.jpg")


def logisticde(path,x,y):
    z = 0
    encryptedImage = img.imread(path)
    height = encryptedImage.shape[0]
    width = encryptedImage.shape[1]
    generatedKey = key.logistic_key(x, y, height*width) 
    decryptedImage = np.zeros(shape=[height, width, 3], dtype=np.uint8)

    # print(height,width)
    for i in range(height):
        for j in range(width):
            decryptedImage[i, j] = encryptedImage[i, j].astype(int) ^ generatedKey[z]
            # print(i,j)
            z += 1
    deimg = Image.fromarray(decryptedImage)
    deimg.save("decryptedImage.jpg")

# orimg= "Original.jpg"
# logisticen(orimg,0.5,3.95)
# enimg="encryptedImage.jpg"
# logisticde(enimg,0.5,3.95)