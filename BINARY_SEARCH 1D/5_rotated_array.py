def search( nums, target):
        n=len(nums)
        low=0
        high=n-1
        while (low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<=nums[high]:
                if nums[mid]<=target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
            else:
                if nums[low]<=target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
        return -1
            

def main():
    arr=list(map(int,input("enter the array").split()))
    target=int(input("enter the target"))
    print(search(arr,target))


if __name__ == "__main__":
    main()