def merge_sort(arr,low,high):
    if (low<high):
        mid=(low+high)//2
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,high)
        merge(arr,low,mid,high)

def merge(arr,low,mid,high):
    i=low
    j=mid+1
    k=low
    b= [0] * len(arr)
    while(i<=mid and j<=high):
        if arr[i]<=arr[j]:
            b[k] = arr[i]
            i = i+1
            k=k+1
        else:
            b[k] = arr[j]
            j = j+1
            k=k+1

    while i<=mid:
            b[k]=arr[i]
            i = i+1
            k=k+1

    while j<= high:
            b[k]=arr[j]
            j= j+1
            k=k+1
    for k in range ( low , high+1) :
        arr[k]=b[k]
     
def main():
    arr=list(map(int,input("enter the array").split()))
    low=0
    n=len(arr)
    high=n-1    
    merge_sort(arr,low,high)
    print(arr)
if __name__ == "__main__":
    main()