
def x(num,n):
   
    if n > num :
        return 
    print(num)
    num = num - 1 
    x(num ,n)

def main():
    num = int(input("enter the number :"))
    n=1
    x(num , n)

if __name__ == "__main__":
    main()