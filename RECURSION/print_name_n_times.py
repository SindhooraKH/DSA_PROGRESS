# num = int(input("enter the number :"))
# n=0
# def x():
#     global num 
#     global n
#     if n == num :
#         return 
#     print("ashish")
#     n = n+ 1 
#     x()

# def main():

#     x()

# if __name__ == "__main__":
#     main()



def x(num,n):
   
    if n == num :
        return 
    print("ashish")
    n = n+ 1 
    x(num ,n)

def main():
    num = int(input("enter the number :"))
    n=0
    x(num , n)

if __name__ == "__main__":
    main()


