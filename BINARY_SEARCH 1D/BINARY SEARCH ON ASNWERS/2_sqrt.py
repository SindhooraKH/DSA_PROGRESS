def sqrt(n):
    low=0
    high=n
    
    while(low<=high):
        mid=(low+high)//2

        if (mid*mid)<=n:
            low=mid+1  
            ans=mid          

        else:
            high=mid-1
    return ans




def main():
    n=int(input("enter the number"))
    print(sqrt(n))


if __name__ == "__main__":
    main()