def check_arr(arr):
    n=len(arr)
    count=0
    # for i in range (n-1):
    #     if  arr[i]=='b' and arr[i+1]=='a' :
    #         count= count+1
    # return count ==0
    for i in range (n-1):
        if  arr[i]=='b' and arr[i+1]=='a' :
            return False
    return True


def main():
    arr=input("enter the array")
    print(check_arr(arr))
if __name__ == "__main__":
    main()