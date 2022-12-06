#Write a python program to calculate the value of y(x,n)
x=float(input("Enter the value of x"))
n=int(input("Enter the value of n"))

if n==1:
    y=1+x
    print("y=",y)

if n==2:
    y=1+x/n
    print("y=",y)

if n==3:
    y=1+x**n
    print("y=",y)

if n>3 or n<1:
    y=1+nx
    print("y=",y)
