def arr_sort(arr):
    n=len(arr)
    count=0
    for i in range (n):
        if arr[i]> arr[(i+1)%n]:
            count=count +1
    return count<=1



def main():
    arr=list(map(int,input("enter the array").split()))
    print(arr_sort(arr))
if __name__ == "__main__":
    main()