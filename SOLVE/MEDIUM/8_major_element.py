def maj(arr):
    n=len(arr)
    freq={}
    for i in arr:
        freq[i]=freq.get(i,0)+1
    for keys,values in freq.items():
        if values >n//3:
            return keys






def main():
    arr=list(map(int,input("enter the array").split()))
    print(maj(arr))

if __name__ == "__main__":
    main()