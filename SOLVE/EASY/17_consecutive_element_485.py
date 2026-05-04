def max_len(arr):
    count = 0
    maxi=0
    for i in arr:
        if i==1:
            count=count+1
            maxi=max(maxi,count)
        else: 
            count=0
    return maxi





def main():
    arr=list(map(int,input("enter the array").split()))
    print(max_len(arr))
if __name__ == "__main__":
    main()