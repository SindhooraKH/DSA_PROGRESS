def duplicate(arr):
    n=len(arr)
    freq={}
    for i in arr:
        freq[i]=freq.get(i,0)+1
    for keys,values in freq.items():
      if values >=2 :
       return keys
     





def main():
    arr=list(map(int,input("enter the array").split()))
    print(duplicate(arr))
if __name__ == "__main__":
    main()