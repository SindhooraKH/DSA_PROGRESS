def matrix(arr,row,col):
    zero=[]
    for i in range (row):
        for j in range(col):
            if arr[i][j]==0:
                zero.append((i,j))
    for i,j in zero:
        for k in range (row):
            arr[i][k]=0
        for k in range (col):
            arr[k][j]=0
    for row in arr:
        print(row)
    return arr

            
def main():
    arr=[]
    row=int(input("enter the number"))
    col=int(input("enter the number"))
    for i in range (row):
        r=[]
        for j in range(col):
            val=int(input(""))
            r.append(val)
    arr.append(r)
    print(matrix(arr,row,col))
if __name__=="__main__":
    main()