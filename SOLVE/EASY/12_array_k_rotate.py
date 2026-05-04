def arr_rotate(arr,val):
    n=len(arr)
    val=val%n
    arr2=arr.copy()
    for i in range (len(arr)):
        arr[i]=arr2[(i+val)%n]
    return arr
def main():
    arr=list(map(int,input("enter the array").split()))
    val=int(input("enter the key"))
    print(arr_rotate(arr,val))
if __name__ == "__main__":
    main()