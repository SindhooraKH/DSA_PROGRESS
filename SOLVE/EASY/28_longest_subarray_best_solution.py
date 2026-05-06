def longest_subarray(arr, k):
    preSumMap = {}
    total = 0
    maxLen = 0

    for i in range(len(arr)):
        total += arr[i]

        if total == k:
            maxLen = i + 1

        rem = total - k
        if rem in preSumMap:
            maxLen = max(maxLen, i - preSumMap[rem])

        if total not in preSumMap:
            preSumMap[total] = i

    return maxLen


def main():
    arr=list(map(int,input("enter the array").split()))
    print(longest_subarray(arr))
if __name__ == "__main__":
    main()