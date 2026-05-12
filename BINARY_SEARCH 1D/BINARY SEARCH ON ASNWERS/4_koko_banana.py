import math

def koko(arr,h):
    low=1
    n=len(arr)
    high=max(arr)
    ans=high
    while(low<=high):
        mid=(low+high)//2
        hour=total_hour(arr,mid)
        if hour<=h:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans 

def total_hour(arr,mid):
    total=0
    for i in range (len(arr)):
        total=total + math.ceil(arr[i]/mid)
    return total

def main():
    arr=list(map(int,input("enter the array").split()))
    h=int(input("enter the hour"))

    print(koko(arr,h))


if __name__ == "__main__":
    main()