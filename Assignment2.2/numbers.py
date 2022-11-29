#rite a Python program to calculate the sum of three given numbers, if theinputvalues are equal then return three times of their sum.

def numbers():
    x=int(input("Enter the first number"))
    y=int(input("Enter the second number"))
    z=int(input("enter the third number"))
    if x==y==z:
        return 3*(x+y+z)
    else:
        return (x+y+z)

print("The output of the program is",numbers())
