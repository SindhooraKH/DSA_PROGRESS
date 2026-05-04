def longestContinuousSubstring( s):
       count=1
       maxi=1
       for i in range (1,len(s)):
            if ord(s[i])-ord(s[i-1])==1:
                count=count+1
                maxi=max(maxi,count)
            else:
                count=1
       return maxi
def main():
    arr=input("enter the array")
    print(longestContinuousSubstring(arr))
if __name__ == "__main__":
    main()