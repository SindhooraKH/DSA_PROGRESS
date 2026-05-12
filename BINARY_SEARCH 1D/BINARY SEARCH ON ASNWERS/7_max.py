import math

def child(arr,mid):
    total=0
    for i in range (len(arr)):
        total=total+arr[i]//mid
    return total
def div(arr,children):
    low=1
    high=max(arr)
    ans=0
    while(low<=high):
        mid=(low+high)//2
        h=child(arr,mid)
        
        if h>=children:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans


def main():
    arr=list(map(int,input("enter the array").split()))
    children=int(input("enter the number"))
    print(div(arr,children))


if __name__ == "__main__":
    main()