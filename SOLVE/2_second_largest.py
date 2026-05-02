# def largest(arr):
#     n=len(arr)
#     largest= float('-inf')
#     second_large= float('-inf')

#     for i in range(n):
#         largest=max(largest,arr[i])
    
#     for i in range(n):
#         if arr[i] > second_large and arr[i]!= largest :
#             second_large= arr[i]
#     return print(second_large)

# def main():
#     arr=list(map(int,input("enter the array").split()))
#     largest(arr)

# if __name__ == "__main__":
#     main()

def largest(arr):
    n=len(arr)
    largest= float('-inf')
    second_large= float('-inf')

    for i in range(n):
        if arr[i]>largest:
            second_large= largest
            largest=arr[i]
        elif arr[i] > second_large and arr[i]!= largest :
            second_large= arr[i]
    return print(second_large)

def main():
    arr=list(map(int,input("enter the array").split()))
    largest(arr)

if __name__ == "__main__":
    main()