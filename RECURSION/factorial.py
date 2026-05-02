class Solution:
    def function(self, num):
        if num==0 or num==1 :
            return 1
        return num * self.function(num-1)


def main():
    obj = Solution()
    num=int(input ("enter the number"))
    result = obj.function(num)
    print(result)


if __name__ == "__main__":
    main()