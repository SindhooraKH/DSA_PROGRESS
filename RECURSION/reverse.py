class Solution:
    def function(self, l,arr,r):
        if (l >=r):
            return 
        arr[l],arr[r]=arr[r],arr[l]
        return self.function(l+1,arr,r-1)


def main():
    obj = Solution()
    arr =list(map(int, input("enter the elements").split()))
    n=len(arr)
    result = obj.function(0,arr,n-1)
    print(arr)


if __name__ == "__main__":
    main()