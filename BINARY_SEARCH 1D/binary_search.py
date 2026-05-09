def binary_search(arr,target,n):
    low=0
    high=n-1
    while (low<=high):
        mid=(low+high)//2

        if arr[mid]==target:
            return mid
        elif target > arr[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1

def main():
    arr=list(map(int,input("enter the array").split()))
    target=int(input("enter the target"))
    n=len(arr)
   
    print(binary_search(arr,target,n))

if __name__ == "__main__":
    main()