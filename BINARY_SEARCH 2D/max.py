
def matrix(arr,row,col):
    maxi=0
    index=-1
    for i in range (row):
        count=0
        for j in range(col):
            if arr[i][j]==1:
                count=count+1
                if count>maxi:
                    maxi=count
                    index=i
            
    return index
   



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