
def x(num,n):
   
    if n > num :
        return 
    print(n)
    n = n+1 
    x(num ,n)

def main():
    num = int(input("enter the number :"))
    n=1
    x(num , n)

if __name__ == "__main__":
    main()