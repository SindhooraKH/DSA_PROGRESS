def arr_rotate(arr):
    j=arr[0]
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]

    arr[len(arr)-1]=j
    return arr

def main():
    arr=list(map(int,input("enter the array").split()))
    print(arr_rotate(arr))
if __name__ == "__main__":
    main()