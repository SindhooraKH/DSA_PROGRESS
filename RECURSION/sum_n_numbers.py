
# def n(num):
#    if num==0 :
#        return 0
#    return (num+n(num-1))

# def main():
#     num= int(input("enter the number"))
#     print(n(num))
    
# if __name__=="__main__":
#     main()



def n(i,sum):
   if (i<0):
       return sum
   return n(i-1,sum+i)

def main():
    num= int(input("enter the number"))
    print(n(num,0))
    
if __name__=="__main__":
    main()


