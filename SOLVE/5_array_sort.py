# def arr_sort(arr):
#     arr2 = sorted(arr)
#     if arr == arr2 :
#         return print(True)
#     else :
#         return print(False)


# def main():
#     arr=list(map(int,input("enter the array").split()))
#     arr_sort(arr)

# if __name__ == "__main__":
#     main()







def arr_sort(arr):
    n=len(arr)
    for i in range (n-1):
        if arr[i]>= arr[i+1]:
            return False
    return True


def main():
    arr=list(map(int,input("enter the array").split()))
    print(arr_sort(arr))
if __name__ == "__main__":
    main()