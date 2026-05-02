class Solution:
    def function(self, l,word,r):
       if l>=r:
           return True
       if word[l]!= word[r] :
           return False
       return self.function(l+1,word,r-1)
       

def main():
    obj = Solution()
    word=input("enter the string")
    n=len(word)
    result = obj.function(0,word,n-1)
    if result :
        print("palindrome")
    else  :
        print("not palindrome")

if __name__ == "__main__":
    main()