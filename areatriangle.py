import math
print("area of triangle")
choice=int(input("Do you want to calculate the area of the triangle using base and height or using sides enter 1 or 2"))
if choice==1:
    base=float(input("Enter the base of the triangle"))
    height=float(input("Enter the height of the triangle"))
    area=0.5*base*height
    print("The area of the triangle is",area)

elif choice==2:
    a= float(input("Enter the side 1 of the triangle"))
    b= float(input("Enter the side 2 of the triangle"))
    c=float(input("Enter the side 3 of the triangle"))
    s=a+b+c/2
    x=s*(s-a)*(s-b)*(s-c)
    area= math.sqrt(x)
    print("The area of the triangle is",area)

else:
    print("invalid choice")
