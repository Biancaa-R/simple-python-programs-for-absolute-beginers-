#Solving a quadratic equation

import math

a=int(input("enter the coefficient of x2"))
b=int(input("enter the coefficient of x"))
c=int(input("enter the constant"))

root1= (-b+ math.sqrt(b*b-4*a*c))
root1=root1/2*a
root2= (-b - math.sqrt(b*b-4*a*c))/2*a

print("The two roots of the quadratic equation is",root1,root2)
