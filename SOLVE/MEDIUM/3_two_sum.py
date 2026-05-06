def two_sum(arr,k):
    n=len(arr)
    arr.sort()
    right=n-1
    left=0
    while left<right:
        sum1=arr[right]+arr[left]
        if k==sum1:
            return "yes"
        elif sum1<k:
            left=left+1
        else:
            right=right+1
    return "NO"
def main():
    arr=list(map(int,input("enter the array").split()))
    k=int(input("enter the number"))
    print(two_sum(arr,k))

if __name__ == "__main__":
    main()