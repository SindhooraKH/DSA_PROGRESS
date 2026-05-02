def hashing(s, hash_arr):
    for ch in s:
        hash_arr[ord(ch) - ord('a')] += 1


def query(hash_arr):
    q = int(input("Enter number of queries: "))
    
    for _ in range(q):
        c = input("Enter character: ")
        print(hash_arr[ord(c) - ord('a')])


def main():
    s = input("Enter string: ")
    
    hash_arr = [0] * 26   # for a-z
    
    hashing(s, hash_arr)
    query(hash_arr)


if __name__ == "__main__":
    main()