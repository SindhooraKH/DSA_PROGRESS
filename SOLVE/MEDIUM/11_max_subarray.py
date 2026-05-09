def max_subarray(arr):
    # n=len(arr)
    # maxi=float('-inf')
    # result=[]
    # for i in range(n):
    #     total=0
    #     for j in range(i,n):
    #         total = total +arr[j]
    #         if total>maxi:
    #             maxi=total
    #             result=arr[i:j+1]
    #             res=sum(result)
    #     return res

        current_sum = arr[0]
        maximum_sum = arr[0]

        for i in range(1, len(arr)):

            current_sum = max(arr[i], current_sum + arr[i])

            maximum_sum = max(maximum_sum, current_sum)

        return maximum_sum







def main():
    arr=list(map(int,input("enter the array").split()))
    print(max_subarray(arr))
if __name__ == "__main__":
    main()