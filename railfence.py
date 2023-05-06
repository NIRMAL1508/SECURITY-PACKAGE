def railfenceen(arr,key):
    # railMatrix=[["//"]*len(arr)]*key
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
