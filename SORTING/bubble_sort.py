def bubble_sort(arr):
    n=len(arr)
    for i in range(n) :
        for j in range (n-i-1):
            if arr[j]>arr[j+1]:
             arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr



def main():
    arr=list(map(int,input("enter the array").split()))
    print(bubble_sort(arr))

if __name__ == "__main__":
    main()