# def insertion_sort(arr):
#     n=len(arr)
#     for i in range (n):
#             j=i
#             while (j>0 and arr[j-1]> arr[j]):
#                temp=arr[j-1]
#                arr[j-1]=arr[j]
#                arr[j]= temp
#                j= j-1
#     return (arr)


# def main():
#     arr=list(map(int,input("enter the array").split()))
#     print(insertion_sort(arr))

# if __name__ == "__main__":
#     main()



def insertion_sort(arr):
    n=len(arr)
    for i in range (n):
            temp=arr[i]
            j=i-1
            while j>=0 and arr[j]> temp:
              arr[j+1]=arr[j]
              j=j-1
            arr[j+1]=temp
    return (arr)


def main():
    arr=list(map(int,input("enter the array").split()))
    print(insertion_sort(arr))

if __name__ == "__main__":
    main()