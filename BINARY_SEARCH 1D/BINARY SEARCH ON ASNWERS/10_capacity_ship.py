
def weight(arr,mid):
    days=1
    load=0
    for i in range (len(arr)):
        if (load+arr[i])>mid:
            days=days+1
            load=arr[i]
        else:
            load=load+arr[i]
    return days
def ship(arr,days):
    low=max(arr)
    high=sum(arr)
    ans=high
    while(low<=high):
        mid=(low+high)//2
        day=weight(arr,mid)
        if day<=days:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans


def main():
    arr=list(map(int,input("enter the array").split()))
    days=int(input("enter the number"))
    print(ship(arr,days))


if __name__ == "__main__":
    main()