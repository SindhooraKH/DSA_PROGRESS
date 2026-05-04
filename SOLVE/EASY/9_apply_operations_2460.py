def opp(arr):  
    i=0  
    while i < len(arr)-1:
        if arr[i] == arr[i+1] :
                arr[i]= arr[i] *2
                arr[i+1]= 0          # 1 3  3 1 0 becomes 1 6 0 1 0
                i=i+1
        else:
             i=i+1
    shift_zero(arr)

def shift_zero(arr):
    j = 0
    
    # move non-zero elements forward
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1       #in this if example has overwirte 1 6 1 1 0
    
    # fill remaining with zeros
    for i in range(j, len(arr)):
        arr[i] = 0   #starts from j =3 that is 1 6 1 0 0 
    
    return arr
    

def main():
    arr=list(map(int,input("enter the array").split()))
    opp(arr)
    print(shift_zero(arr))
if __name__ == "__main__":
    main()


