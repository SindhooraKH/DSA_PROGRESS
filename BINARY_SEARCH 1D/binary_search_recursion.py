def binary_search(arr,low,high,target):
    
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif target>arr[mid]:
        return binary_search(arr,mid+1,high,target)
    else:
        return binary_search(arr,low,mid-1,target)

def main():
    arr=list(map(int,input("enter the array").split()))
    target=int(input("enter the target"))
    n=len(arr)

    low=0
    high=n-1
   
    print(binary_search(arr,low,high,target))

if __name__ == "__main__":
    main()