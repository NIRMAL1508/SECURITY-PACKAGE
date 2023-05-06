import numpy
from operator import invert
def caesaren(str,k):
    key = int(k)
    temp=list(str)
    #print(key)
    for i in range(0,len(temp)):
        

        temp[i] = chr((ord(temp[i])+key-32)%95 +32)
    
    
    return "".join(temp) 
    
def caesarde(str,k):
    key=int(k)
    temp=list(str)
    
    for i in range(0,len(temp)):

        temp[i] = chr((ord(temp[i])-key-32)%95 +32)
    
    
    return "".join(temp) 

def monoalphen(str):
    temp=""
    key="qwertyuiopasdfghjklzxcvbnm"
 
    for i in range(0,len(str)):
        char=str[i]
      
        try:
            temp+= key[ord(char)-97]
        except:
            print(char)
    return temp

# def readkey():
#     file=open("key.txt","r")
#     return file.read()

def monoalphde(str):
    temp=""
    key="qwertyuiopasdfghjklzxcvbnm"
   
    for i in range(0,len(str)):
        char=str[i]
        # if(char.isupper()):
        try:
            temp+=chr(key.find(char) + 97)
        except:
            print(char)
    return temp

def transposen(str,key):
    arr=[]
    j=0
    temp=[]
    for i in range(0,len(str)):
        if(j<int(key[0])):
            temp.append(str[i])
            j+=1
        else:
            arr.append(temp)
            temp=[]
            temp.append(str[i])
            j=1
        if(i==len(str)-1):
            for i in range(0,int(key[0])-j):
                temp.append(' ')
            arr.append(temp)
    str=""        
    for i in range(0,int(key[0])):
        j=0
        try:
            while(arr[j][i]):
                str+=arr[j][i]
                j+=1
        except:
            continue
    i ="% s"%len(arr)
    key.append(i)   
    print(arr)    
    return str,key
    
def transposde(str,key):
    c="% s"%key[0]
    r="% s"%key[1]
    arr=[]
    j=0
    temp=[]
    for i in range(0,len(str)):
        if(j<int(key[1])):
            temp.append(str[i])
            j+=1
        else:
            arr.append(temp)
            temp=[]
            temp.append(str[i])
            j=1
        if(i==len(str)-1):
                arr.append(temp)
    print(arr)
    str=""        
    for i in range(0,int(key[1])):
        j=0
        try:
            while(arr[j][i]):
                str+=arr[j][i]
                j+=1
        except:
            continue
            
    return str

def toLowerCase(text):
    return text.lower()
  
 
 
def removeSpaces(text):
    newText = ""
    for i in text:
        if i == " ":
            continue
        else:
            newText = newText + i
    return newText
 
 
def Diagraph(text):
    Diagraph = []
    group = 0
    for i in range(2, len(text), 2):
        Diagraph.append(text[group:i])
 
        group = i
    Diagraph.append(text[group:])
    return Diagraph
 
 
 
def FillerLetter(text):
    k = len(text)
    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    else:
        for i in range(0, k-1, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    return new_word
 
 
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
 
 
def generateKeyTable(word, list1):
    key_letters = []
    for i in word:
        if i not in key_letters:
            key_letters.append(i)
 
    compElements = []
    for i in key_letters:
        if i not in compElements:
            compElements.append(i)
    for i in list1:
        if i not in compElements:
            compElements.append(i)
 
    matrix = []
    while compElements != []:
        matrix.append(compElements[:5])
        compElements = compElements[5:]
    # print(matrix)
    return matrix
 
 
def search(mat, element):
    for i in range(5):
        for j in range(5):
            if(mat[i][j] == element):
                return i, j
 
 
def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1c == 4:
        char1 = matr[e1r][0]
    else:
        char1 = matr[e1r][e1c+1]
 
    char2 = ''
    if e2c == 4:
        char2 = matr[e2r][0]
    else:
        char2 = matr[e2r][e2c+1]
 
    return char1, char2

def decrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1c == 0:
        char1 = matr[e1r][4]
    else:
        char1 = matr[e1r][e1c-1]
 
    char2 = ''
    if e2c == 0:
        char2 = matr[e2r][4]
    else:
        char2 = matr[e2r][e2c-1]
 
    return char1, char2

def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1r == 4:
        char1 = matr[0][e1c]
    else:
        char1 = matr[e1r+1][e1c]
 
    char2 = ''
    if e2r == 4:
        char2 = matr[0][e2c]
    else:
        char2 = matr[e2r+1][e2c]
 
    return char1, char2
 
def decrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1r == 0:
        char1 = matr[4][e1c]
    else:
        char1 = matr[e1r-1][e1c]
 
    char2 = ''
    if e2r == 0:
        char2 = matr[4][e2c]
    else:
        char2 = matr[e2r-1][e2c]
 
    return char1, char2

def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    char1 = matr[e1r][e2c]
 
    char2 = ''
    char2 = matr[e2r][e1c]
 
    return char1, char2
 
def decrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    char1 = matr[e1r][e2c]
 
    char2 = ''
    char2 = matr[e2r][e1c]
 
    return char1, char2

def encryptByPlayfairCipher(Matrix, plainList):
    CipherText = []
    for i in range(0, len(plainList)):
        c1 = 0
        c2 = 0
        ele1_x, ele1_y = search(Matrix, plainList[i][0])
        ele2_x, ele2_y = search(Matrix, plainList[i][1])
 
        if ele1_x == ele2_x:
            c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            # Get 2 letter cipherText
        elif ele1_y == ele2_y:
            c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = encrypt_RectangleRule(
                Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
 
        cipher = c1 + c2
        CipherText.append(cipher)
    return CipherText
 
def playfairen(str,key) :
    text_Plain = str
    text_Plain = removeSpaces(toLowerCase(text_Plain))
    PlainTextList = Diagraph(FillerLetter(text_Plain))
    if len(PlainTextList[-1]) != 2:
        PlainTextList[-1] = PlainTextList[-1]+'z'
    
    
    key = toLowerCase(key)
    Matrix = generateKeyTable(key, list1)
    
    CipherList = encryptByPlayfairCipher(Matrix, PlainTextList)
    
    CipherText = ""
    for i in CipherList:
        CipherText += i
    return CipherText

def decryptByPlayfairCipher(Matrix, EncryptedList):
    MsgText = []
    for i in range(0, len(EncryptedList)):
        c1 = 0
        c2 = 0
        ele1_x, ele1_y = search(Matrix, EncryptedList[i][0])
        ele2_x, ele2_y = search(Matrix, EncryptedList[i][1])
 
        if ele1_x == ele2_x:
            c1, c2 = decrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            # Get 2 letter cipherText
        elif ele1_y == ele2_y:
            c1, c2 = decrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = decrypt_RectangleRule(
                Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
 
        cipher = c1 + c2
        MsgText.append(cipher)
    return MsgText

def playfairde(str,key):
    text_Plain = str
    Encryptedtextlist = Diagraph(FillerLetter(text_Plain))
    Matrix = generateKeyTable(key, list1)
    msglist = decryptByPlayfairCipher(Matrix,Encryptedtextlist)

    message=""
    for i in msglist:
       message += i
    return message

def railfenceen(arr,key):
    railMatrix=[["\n" for i in range(len(arr))]for j in range(key)]
    # for i in range(len(railMatrix)):
    #     for j in range(len(railMatrix[i])):
    #         print(railMatrix[i][j])
    row,col,k=0,0,-1
    enresult=""
    for i in range(len(arr)):
        railMatrix[row][col]=arr[i]
        col+=1
        if row==0 or row==key-1:
            k=k*(-1)
        row=row+k
    # print(railMatrix)    
    for i in range(key):
        for j in range(len(arr)):
            if railMatrix[i][j]!="\n":
                # print(railMatrix[i][j])
                enresult+=railMatrix[i][j]
    return enresult                

def railfencede(enarr,key):
        railMatrix=[["//" for i in range(len(enarr))]for j in range(key)]
        row,col,k,m=0,0,-1,0
        result=""
        for i in range(len(enarr)):
            railMatrix[row][col]="*"
            col+=1
            if row==0 or row==key-1:
                k=k*(-1)
            row=row+k
        for i in range(key):
            for j in range(len(enarr)):
                if railMatrix[i][j]=="*":
                    railMatrix[i][j]=enarr[m]
                    m+=1
        row,col=0,0
        k=-1
        for i in range(len(enarr)):
            result+=railMatrix[row][col]
            col+=1
            if row==0 or row==key-1:
                k=k*(-1)
            row=row+k       
        return result

def invmod26(arr):
    detmod26=(arr[0][0]*(arr[1][1]*arr[2][2] - arr[1][2]*arr[2][1])) - (arr[0][1]*(arr[1][0]*arr[2][2] - arr[2][0]*arr[1][2])) + (arr[0][2]*(arr[1][0]*arr[2][1] - arr[2][0]*arr[1][1]))
    
    detmod26=detmod26%26
    
    for factor in range(0,26):
        if((factor*detmod26)%26 == 1):
            break
    
#matrix is a numpy 3x3 array and if any other stuff is passed it will throw an error.
    matrix=numpy.array(arr)
    mtrx = matrix.ravel()  #ravel() converts 2d array to 1d. Just to make things easier.
    A= (+((mtrx[4]*mtrx[8])-(mtrx[5]*mtrx[7])))%26
    B= (-((mtrx[3]*mtrx[8])-(mtrx[5]*mtrx[6])))%26
    C= (+((mtrx[3]*mtrx[7])-(mtrx[6]*mtrx[4])))%26
    D= (-((mtrx[1]*mtrx[8])-(mtrx[2]*mtrx[7])))%26
    E= (+((mtrx[0]*mtrx[8])-(mtrx[2]*mtrx[6])))%26
    F= (-((mtrx[0]*mtrx[7])-(mtrx[1]*mtrx[6])))%26
    G= (+((mtrx[1]*mtrx[5])-(mtrx[2]*mtrx[4])))%26
    H= (-((mtrx[0]*mtrx[5])-(mtrx[2]*mtrx[3])))%26
    I= (+((mtrx[0]*mtrx[4])-(mtrx[1]*mtrx[3])))%26
    #Convert back to 3x3 matrix format
    cofactor = numpy.array([[A, B, C], 
                         [D, E, F], 
                         [G, H, I]])
    #Formula for adjoint
    arr = cofactor.T
    for i in range(0,3):
        for j in range(0,3):
            arr[i][j]= (factor*arr[i][j])%26
    return arr

def hillkey(key):
    keyMatrix = [[0] * 3 for i in range(3)]
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
          
    return keyMatrix

def Hillen(message, key):
    messageVector = [[0] for i in range(3)]
    
    keyMatrix=hillkey(key)
    
    
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65
 
    cipherMatrix = [[0] for i in range(3)]
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] *
                                       messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26

    CipherText = []
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))
 
    return ''.join(CipherText)

def Hillde(enmsg,key):
    enmessageVector = [[0] for i in range(3)]
    keyMatrix=hillkey(key)
    keyMatrix=invmod26(keyMatrix)
    for i in range(3):
        enmessageVector[i][0] = ord(enmsg[i]) % 65
    cipherMatrix = [[0] for i in range(3)]
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] *
                                       enmessageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26
    CipherText = []
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))
    str=""
    for i in range(0,len(CipherText)):
        str= str+CipherText[i]
    return str


       
    