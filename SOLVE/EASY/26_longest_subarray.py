def longest(arr, k):
    n = len(arr)
    max_len = 0
    result = []

    for i in range(n):
        total = 0
        for j in range(i, n):
            total += arr[j]

            if total == k:
                if (j - i + 1) > max_len:
                    max_len = j - i + 1
                    result = arr[i:j+1]

    return result

def main():
    arr=list(map(int,input("enter the array").split()))
    k=int(input("enter the number"))
    print(longest(arr,k))
if __name__ == "__main__":
    main()