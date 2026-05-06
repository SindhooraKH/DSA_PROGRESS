def two_sum(arr,k):
    n=len(arr)
    hash_map=[]
    for i in range(len(arr)):
        total=k-arr[i]
        if total in hash_map:
            j=hash_map.index(total)
            return (j, i)
        hash_map.append(arr[i])
    return (-1,-1)


def main():
    arr=list(map(int,input("enter the array").split()))
    k=int(input("enter the number"))
    print(two_sum(arr,k))

if __name__ == "__main__":
    main()