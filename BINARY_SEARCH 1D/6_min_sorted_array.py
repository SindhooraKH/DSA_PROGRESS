def search( nums):
        n=len(nums)
        low=0
        high=n-1
        while (low<=high):
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]
            

def main():
    arr=list(map(int,input("enter the array").split()))
    print(search(arr))


if __name__ == "__main__":
    main()