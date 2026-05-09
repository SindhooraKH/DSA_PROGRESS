def ceil_search(arr,target):
    n=len(arr)
    low=0
    high=n-1
    ans=n
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=target:
            ans=mid

            high=mid-1
        else:
            low=mid+1
    return arr[ans]
def floor_search(arr,target):
    n=len(arr)
    low=0
    high=n-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<=target:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return arr[ans]


def main():
    arr=list(map(int,input("enter the array").split()))
    target=int(input("enter the target"))
    print(ceil_search(arr,target))
    print(floor_search(arr,target))


if __name__ == "__main__":
    main()