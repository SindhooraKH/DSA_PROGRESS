def remove_dup(arr):
    # result = []
    
    # for x in arr:
    #     if x not in result:
    #         result.append(x)
    
    # print(result)

    i=0
    while i < len(arr)-1:
        if arr[i+1]== arr[i]:
                del arr[i]
        else:
            i=i+1
    return arr

def main():
    arr=list(map(int,input("enter the array").split()))
    print(remove_dup(arr))
if __name__ == "__main__":
    main()