
def move(arr):
    # j=0
    # count=1
    # for i in range(len(arr)):
    #     if arr[i]!=0 :
    #         arr[j]=arr[i]
    #         j=j+1

    # for j in range(j,len(arr)):
    #     arr[i]=0
    # return arr
    for _ in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i]==0:
                arr[i],arr[i+1]= arr[i+1],arr[i]
            
    return arr




def main():
    arr=list(map(int,input("enter the array").split()))
    print(move(arr))
if __name__ == "__main__":
    main()