def longest(arr):
    n=len(arr)
    max_length=0
    result=[]
    for i in range(n):
        total=0
        for j in range(i,n):
            total=total+arr[j]
        if total==0:
            if (j-i+1)>max_length:
                max_length=j-i+1
                result=arr[i:j+1]
    return len(result)
       


def main():
    arr=list(map(int,input("enter the array").split()))
    print(longest(arr))
if __name__ == "__main__":
    main()