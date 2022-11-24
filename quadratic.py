#Python program to solve a quadratic equation
import math
a=int(input("Enter the coefficient of x2"))
b=int(input("Enter the coefficient of x"))
c=int(input("Enter the constant term"))

root1= -b - math.sqrt(b*b-4*a*c)
root1=root1/2*a


root2= -b + math.sqrt(b*b-4*a*c)
root2=root2/2*a

print("The roots of the quadratic equation is",root1," ",root2)
