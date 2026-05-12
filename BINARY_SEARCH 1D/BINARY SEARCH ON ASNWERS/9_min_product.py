import math
def thresh(arr,mid):
    total=0
    for i in range (len(arr)):
        total=total+math.ceil(arr[i]/mid)
    return total
def div(arr,n):
    low=1
    high=max(arr)
    ans=high
    while(low<=high):
        mid=(low+high)//2
        h=thresh(arr,mid)
        if h<=n:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans


def main():
    arr=list(map(int,input("enter the array").split()))
    n=int(input("enter the number"))
    print(div(arr,n))


if __name__ == "__main__":
    main()