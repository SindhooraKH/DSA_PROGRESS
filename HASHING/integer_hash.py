def hashing(arr, hash_arr):
    for num in arr:
        hash_arr[num] += 1


def query(hash_arr):
    q = int(input("Enter number of queries: "))
    
    for _ in range(q):
        x = int(input("Enter number: "))
        print(hash_arr[x])


def main():
    arr = list(map(int, input("Enter array: ").split()))
    
    hash_arr = [0] * 13   # adjust size based on max value
    
    hashing(arr, hash_arr)
    query(hash_arr)


if __name__ == "__main__":
    main()







    