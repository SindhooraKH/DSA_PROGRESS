def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
         return i  
        else:
           return -1      

def main():
    arr=list(map(int,input("enter the array").split()))
    key=int(input("enter the number to search"))
    print(linear_search(arr,key))
if __name__ == "__main__":
    main()