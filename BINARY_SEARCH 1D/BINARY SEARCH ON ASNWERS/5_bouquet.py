
def bouquet(arr,m,k):
    n=len(arr)
    low=min(arr)
    high=max(arr)
    while(low<=high):
        if m*k > n:
            return -1
        

def main():
    arr=list(map(int,input("enter the array").split()))
    m=int(input("enter the bouquet"))
    k=int(input("enter the adjacent number"))

    print(bouquet(arr,m,k))


if __name__ == "__main__":
    main()