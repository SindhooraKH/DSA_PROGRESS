def sqrt(n):
    ans=1
    for i in range (n):
        if (i*i)<=n :
            ans=i
        else:
            break
    return ans





def main():
    n=int(input("enter the number"))
    print(sqrt(n))


if __name__ == "__main__":
    main()