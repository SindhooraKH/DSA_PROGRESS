def missing(arr):
    n=len(arr)
    total=0
    sum1=0
    for i in arr:
        total=total+i
    for i in range (1,n+1):
        sum1=sum1+i
    return sum1-total


def main():
    arr=list(map(int,input("enter the array").split()))
    print(missing(arr))
if __name__ == "__main__":
    main()