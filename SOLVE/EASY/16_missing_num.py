def miss(arr):
   n=len(arr)
   arr2= [ ]

   for i in range(1, n+1):
       arr2.append(i)
  
   for i in arr2:
       if i not in arr:
        return i    
 

def main():
    arr=list(map(int,input("enter the array").split()))
    print(miss(arr))
if __name__ == "__main__":
    main()