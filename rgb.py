import random
from PIL import Image
import numpy as np
from numpy import asarray

def rgben(str,key):
    pixels = []
    l=len(str)
    temp = [0,0,0]
    j=0
    for i in range(0,l):
            if(j<3):
                temp[j]=ord(str[i])
                j+=1
                pixels.append(temp)
                temp=[0,0,0]
                continue
            else:
                temp=[0,0,0]
                temp[0]=ord(str[i])
                j=1
                pixels.append(temp)
                temp=[0,0,0]
            if(i==len(str)-1):
                pixels.append(temp)
                temp=[0,0,0]

    if(len(pixels)%key==0):
        r=int(len(pixels)/key)
    else:
        m= key - len(pixels)%key
        for i in range(0,m):
            if(i==0):
                pixels.append([1,1,1])
                continue
            pixels.append([0,0,0])
        r=int(len(pixels)/key)
    l=len(pixels)
    # temp.append(pixels[i])
    #             j=1
    #         if(i==len(str)-1):
    #             for k in range(j,sq):
    #                 temp.append([0,0,0])
    #             res.append(temp)

    a = np.array(pixels).reshape(r,key,3)

          
    pixels=a
    
    for i in range(0,len(pixels)):
        for j in range(0,len(pixels[i])):
            for k in range(0,len(pixels[i][j])):
                if(pixels[i][j][k]==0):
                    pixels[i][j][k]=random.randint(2,256)
    print(pixels)
    transpos = [[]]
    for i in range(0,key):
        for j in range(0,r):
            transpos[0].append(pixels[j][i])
       

    pixels = transpos
    print(pixels)
   
    
    array = np.array(pixels, dtype=np.uint8)
    
    # Use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image.save('new.png')

def rgbde(img,key):
    img = Image.open(img)
    numpydata = asarray(img)
    temp=[]
    arr=[]
    j=0
    l=len(numpydata[0])
    print(l)
    r=int(l/key)
    arr = np.array(numpydata).reshape(key,r,3)

    str=""
    print(arr)
    k=0
    for i in range(0,r):
        for j in range(0,key):
            if(arr[j][i][1]!=1):
                if(k<3):
                    str+=chr(arr[j][i][k])
                    k+=1
                else:
                    str+=chr(arr[j][i][0])
                    k=1
            else:
                break  
        
    return str
    


# str=input()
# key=int(input())
# rgben(str,key)
# img='new.png'
# print(rgbde(img,key))