# def remove_dup(arr):
# #    count=1
# #    i=0
# #    for j in range (1,len(arr)):
# #        if arr[j]==arr[j-1]:
# #            count= count + 1
# #        else:
# #            count=1
# #        if count <=2:
# #            i=i+1
# #            arr[i]=arr[j]
# #    return arr[:i+1]

def remove_dup(self, arr):
        n = len(arr)
        if n<=2:
            return n
        start = 1
        for i in range(2,len(arr)):
            if arr[i]!=arr[start-1]:
                start+=1
                arr[start] = arr[i]
        
        return start+1
def main():
    arr=list(map(int,input("enter the array").split()))
    print(remove_dup(arr))
if __name__ == "__main__":
    main()