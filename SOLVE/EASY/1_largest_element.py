def largest(arr):
    n=len(arr)
    max_num= arr[0]
    for i in range (n):
        if arr[i]> max_num:
            max_num= arr[i]
    return print(max_num)




def main():
    arr=list(map(int,input("enter the array").split()))
    largest(arr)

if __name__ == "__main__":
    main()



# "' second method "'
# def largest(arr):
#     n=len(arr)
#     largest= float('-inf')


#     for i in range(n):
#         largest=max(largest,arr[i])
#     return print (largest)


# def main():
#     arr=list(map(int,input("enter the array").split()))
#     largest(arr)

# if __name__ == "__main__":
#     main()


