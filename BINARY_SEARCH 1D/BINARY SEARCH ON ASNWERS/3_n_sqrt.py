def sqrt(n,k):
    low=0
    high=n
    
    while(low<=high):
        mid=(low+high)//2
        if mid**k==n:
            return mid

        elif (mid**k)<=n:
            low=mid+1  
            ans=mid          

        else:
            high=mid-1
    return -1




def main():
    n=int(input("enter the number"))
    k=int(input("enter the nth root"))
    print(sqrt(n,k))


if __name__ == "__main__":
    main()