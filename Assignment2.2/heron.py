program to find the area of a triangle whose sides are given

while True:
    a= float(input("Enter the side 1 of the triangle"))
    b= float(input("Enter the side 2 of the triangle"))
    c=float(input("Enter the side 3 of the triangle"))
    s=a+b+c/2
    x=s*(s-a)*(s-b)*(s-c)
    area= math.sqrt(x)
    print("The area of the triangle is",area)

    choice=input("Do you want to calculate the area of more triangles? y/n")
    if choice in ["n","N"]:
        break
 

