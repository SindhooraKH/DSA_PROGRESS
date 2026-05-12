# def main():
#    arr=[]
#    n=int(input("enter the  number"))
#    for i in range(n):
#        row=list(map(int,input("enter the array").split()))
#        arr.append(row)
#    print(arr)
# if __name__=="__main__":
#     main()

arr = []
rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))

for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input())
        row.append(val)
    arr.append(row)
print(arr)