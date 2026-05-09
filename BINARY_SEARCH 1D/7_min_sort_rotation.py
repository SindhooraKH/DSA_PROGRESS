def search(arr):
    n=len(arr)
    low=0
    high=n-1

    while low<high:
        mid=(low+high)//2
        if arr[mid] >arr[high]:
            low=mid+1
        else:
            high=mid
    return low




def main():
    arr=list(map(int,input("enter the array").split()))
    print(search(arr))


if __name__ == "__main__":
    main()