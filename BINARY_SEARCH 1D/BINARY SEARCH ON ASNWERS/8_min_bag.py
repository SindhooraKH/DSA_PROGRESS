
def bags(arr,mid):
    total=0
    for i in range (len(arr)):
        total=total+(arr[i]-1)//mid
    return total
def div(arr,maxop):
    low=1
    high=max(arr)
    ans=high
    while(low<=high):
        mid=(low+high)//2
        bag=bags(arr,mid)
        if bag<=maxop:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans


def main():
    arr=list(map(int,input("enter the array").split()))
    maxop=int(input("enter the number"))
    print(div(arr,maxop))


if __name__ == "__main__":
    main()