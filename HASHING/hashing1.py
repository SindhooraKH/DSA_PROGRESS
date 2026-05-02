# def hashing(arr,hash_arr,n):
#     for i in range (n) :
#         hash_arr[arr[i]] += 1


# def query(hash_arr) :
#    q = int(input("enter the query number"))

#    for _ in range(q):
#         x = int(input("enter number to search"))
#         print(hash_arr[x])

# def main():
#     arr = list(map(int,input("enter the array").split()))
#     n=len(arr)
#     hash_arr= [0]  * 13
#     hashing(arr,hash_arr,n)
#     query(hash_arr)

# if __name__=="__main__":
#     main()

#for character using frq
# def hashing(s):
#     freq = {}
#     for ch in s:
#         freq[ch] = freq.get(ch, 0) + 1
#     return freq


# def query(freq):
#     q = int(input("Enter queries: "))
#     for _ in range(q):
#         x = input("Enter char: ")
#         print(freq.get(x, 0))

# def main():
#     s = input("Enter string: ")
#     freq = hashing(s)
#     query(freq)

# if __name__=="__main__":
#     main()

def hashing(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq



def query(freq):
    q = int(input("Enter queries: "))
    for _ in range(q):
        x = int(input("Enter number: "))
        print(freq.get(x, 0))

def main():
    arr = list(map(int, input("Enter array: ").split()))
    freq = hashing(arr)
    query(freq)

if __name__=="__main__":
    main()