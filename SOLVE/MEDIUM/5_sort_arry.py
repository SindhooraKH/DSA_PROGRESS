def sort(arr):
    n=len(arr)
    mid=0
    low=0
    high=n-1
    while mid<=high:
        if arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]
            low+=1
            mid+=1
        elif arr[mid]==2:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
        else:
            mid+=1
    return arr


def main():
    arr=list(map(int,input("enter the array").split()))
    print(sort(arr))

if __name__ == "__main__":
    main()