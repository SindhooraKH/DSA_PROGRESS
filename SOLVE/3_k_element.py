def largest(arr,k):
    n=len(arr)
    #arr.sort()
    arr.sort(key=int)  # cnvert string to int and does it 
    return print(arr[n-k])

def main():
    #arr=list(map(int,input("enter the array").split()))
    arr=input("enter the array").split()

    k= int(input("enter the number to find"))

    largest(arr,k)
if __name__ == "__main__":
    main()