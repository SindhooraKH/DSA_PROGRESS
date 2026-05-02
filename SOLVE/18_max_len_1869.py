def max_len(arr):
    count1= 0
    count0=0
    max1=0
    max0=0
    
    for i in arr:
        if i=='1':
            count1=count1+1
            max1=max(max1,count1)
        else: 
            count1=0
    for i in arr:
        if i=='0':
            count0=count0+1
            max0=max(max0,count0)
        else: 
            count0=0
    if max(max1,max0) > max1 :
        return True
    else:
        return False


    








def main():
    arr=list(map(int,input("enter the array").split()))
    print(max_len(arr))
if __name__ == "__main__":
    main()