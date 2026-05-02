def maxPower(s):
        count=1
        maxi=1
        for i in range(1,len(s)):
            if s[i] ==s[i-1]:
                 count=count+1
                 maxi=max(maxi,count)
            else:
                 count=1
        return maxi
def main():
    s=input("enter the array")
    print(maxPower(s))
if __name__ == "__main__":
    main()