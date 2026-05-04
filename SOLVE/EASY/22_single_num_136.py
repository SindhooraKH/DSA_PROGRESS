def singleNumber( nums):
       freq= {}
       for i in nums:
         freq[i]=freq.get(i,0)+1
       for key,value in freq.items():
           if value==1:
               return key
        
def main():
    arr=list(map(int,input("enter the array").split()))
    print(singleNumber(arr))
if __name__ == "__main__":
    main()