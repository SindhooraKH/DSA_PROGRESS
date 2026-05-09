def search(arr,target):
    arr.sort()
    n=len(arr)
    low=0
    high=n-1
    ans=n
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=target:
            high=mid-1
            ans=mid
        else:
            low=mid+1
    return ans
        

def main():
    arr=list(map(int,input("enter the array").split()))
    target=int(input("enter the target"))
   
   
    print(search(arr,target))

if __name__ == "__main__":
    main()