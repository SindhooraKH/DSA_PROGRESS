def minimumChairs(s):
        count1= 0
        maxi=0
        for i in s:
            if i=='E':
                count1=count1+1
                maxi=max(count1,maxi)
            else: 
                count1=count1-1
        return maxi




def main():
    arr=input("enter the array")
    print(minimumChairs(arr))
if __name__ == "__main__":
    main()