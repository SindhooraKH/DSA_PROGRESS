def buy_sell(arr):
    min_price = arr[0]
    max_profit = 0

    for i in range(1, len(arr)):

        min_price = min(min_price, arr[i])

        profit = arr[i] - min_price

        max_profit = max(max_profit, profit)

    return max_profit

def main():
    arr=list(map(int,input("enter the array").split()))
   
    print(buy_sell(arr,))

if __name__ == "__main__":
    main()