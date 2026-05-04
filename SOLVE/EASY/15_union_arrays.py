def union(arr1,arr2):
    arr3=arr1+arr2

# check arr2
    for x in arr2:
        if x not in arr1:
            arr1.append(x)
    return arr1


    # for i in arr3:
    #     if i not in arr4:
    #         arr4.append(i)


def main():

    arr1=list(map(int,input("enter the array").split()))
    arr2=list(map(int,input("enter the array").split()))
    print(union(arr1,arr2))
if __name__ == "__main__":
    main()