class Solution:
    def function(self, num):
        if num==0 :
            return 0
        if num==1:
            return 1
        return self.function(num-1) + self.function(num-2)


def main():
    obj = Solution()
    num=int(input ("enter the number"))
    result = obj.function(num)
    print(result)


if __name__ == "__main__":
    main()