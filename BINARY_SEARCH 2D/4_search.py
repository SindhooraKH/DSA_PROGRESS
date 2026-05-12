class Solution:

    def search(self, arr, target):

        n = len(arr)
        m = len(arr[0])

        low = 0
        high = n * m - 1

        while low <= high:

            mid = (low + high) // 2

            row = mid // m
            col = mid % m

            if arr[row][col] == target:
                return True

            elif arr[row][col] < target:
                low = mid + 1

            else:
                high = mid - 1

        return False


def main():

    matrix = []

    r = int(input("enter rows: "))
    c = int(input("enter cols: "))
    target = int(input("enter target: "))

    for i in range(r):

        row = []

        for j in range(c):
            val = int(input())
            row.append(val)

        matrix.append(row)

    s = Solution()

    print(s.search(matrix, target))


if __name__ == "__main__":
    main()