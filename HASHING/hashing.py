#brute force approach

arr= list(map(int,input("enter the array").split()))
count=0
n=len(arr)
num = int(input("enter the number"))
for i in range (n):
     if arr[i]== num :
          count=count+1
print ("the number arrived", count)