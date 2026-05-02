def x(num):
    if num<1:
      return
    print(num)
    x(num-1)
    

def main():
    num = int(input("enter the number: "))
    x(num)

if __name__ == "__main__":
    main()