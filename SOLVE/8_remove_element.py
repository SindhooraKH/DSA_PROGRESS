def remove_ele(arr,val):
    # i=0
    # while i < len(arr):
    #     if arr[i]==val:
    #             del arr[i]
    #     else:
    #         i=i+1
    # return arr
    k = 0
        
    for i in range(len(arr)):
        if arr[i] != val:
                arr[k] = arr[i]
                k += 1
        
    return k

def main():
    arr=list(map(int,input("enter the array").split()))
    val=int(input("enter the number"))
    print(remove_ele(arr,val))
if __name__ == "__main__":
    main()