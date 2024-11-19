def setornot(number,n):
    mask=1
    if (n & mask)==1 or (n & mask)==0:
        if number & (1<<(n-1)):
            print("SET")
        else:
            print("NOT SET")
number=int(input("Enter a number:"))
n=int(1)
setornot(number,n)