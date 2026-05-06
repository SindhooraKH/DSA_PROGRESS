def fre(arr,k):
    freq={}
    for i in arr:
        freq[i]=freq.get(i,0)+1  #calculate the freq 1:3 2:2 3:1
    bucket=[[] for i in range (len(arr)+1)] #create buckets [] [] [] [] [][][]
    result=[]
    for keys,values in freq.items():
        bucket[values].append(keys)  #bucket [], [3], [2], [1], [], [], []
    for i in range (len(bucket)-1,1,-1):
        for i in bucket[i]:
            result.append(i)                  
        if len(result)==k:
            return result



    


def main():
    arr=list(map(int,input("enter the array").split()))
    k=int(input("enter the number"))
    print(fre(arr,k))

if __name__ == "__main__":
    main()