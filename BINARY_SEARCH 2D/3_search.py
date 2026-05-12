
def matrix(arr,row,col,n):
    for i in range (row):
        for j in range(col):
            if arr[i][j]==n:
                return True
            
    return False
   



def main():
    arr=[]
    row=int(input("enter the number of rows"))
    col=int(input("enter the number of cols"))
    n=int(input("enter the number to search"))
    for i in range (row):
        r=[]
        for j in range(col):
            val=int(input(""))
            r.append(val)
        arr.append(r)
    print(matrix(arr,row,col,n))

if __name__=="__main__":
    main()