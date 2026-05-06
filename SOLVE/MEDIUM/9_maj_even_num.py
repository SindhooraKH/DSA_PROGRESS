def maj(arr):
    freq={}
    max_freq=0
    for i in arr:
        if i%2 ==0:
            freq[i]=freq.get(i,0)+1

    for key, value in freq.items():
        if value > max_freq:
            max_freq = value
            result = key
        elif value == max_freq:
            result = min(result, key)

    return result

def main():
    arr=list(map(int,input("enter the array").split()))
    print(maj(arr))

if __name__ == "__main__":
    main()