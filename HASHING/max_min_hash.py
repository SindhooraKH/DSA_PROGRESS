def hashing(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq



def query(freq):
    print(max(freq, key=freq.get))
    print(min(freq, key=freq.get))
    


def main():
    arr = list(map(int, input("Enter array: ").split()))
    freq = hashing(arr)
    query(freq)

if __name__=="__main__":
    main()