def first_search(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            ans = mid
            high = mid - 1

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return ans


def last_search(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            ans = mid
            low = mid + 1

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return ans


def search(arr, target):
    first = first_search(arr, target)
    last = last_search(arr, target)

    return [first, last]


def main():
    arr = list(map(int, input("enter the array: ").split()))
    target = int(input("enter the target: "))

    print(search(arr, target))


if __name__ == "__main__":
    main()