def last_occurence(arr,target):
    maxi=[]
    for i in range (len(arr)):
          if arr[i]==target :
            maxi.append(i)
          if arr[i]!=target :
              return -1,-1
    return maxi[0], maxi[-1]







# 3, 4, 13, 13, 13, 20, 40




def main():
    arr=list(map(int,input("enter the array").split()))
    target=int(input("enter the target"))
    print(last_occurence(arr,target))


if __name__ == "__main__":
    main()