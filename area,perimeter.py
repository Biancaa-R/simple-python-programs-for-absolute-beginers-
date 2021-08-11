radius=float(input("enter the value of radius in centimeters"))
print("type 1 to calculate the area of the circle")
print("type 2 to calculate the circumference of the circle")

choice= int(input("enter your choice 1 or 2 : "))
step2()


def to_find_area():
    area= 3.1415926*radius*radius
    float(area)
    print("The area of a circle with radius",radius,"is",area)

def to_find_circumference():
    circumference=2*3.1415926*radius
    float(circumference)
    print("the circumference of the circle with radius",radius,"is",circumference)

def step2():
    
    if choice==1:
        print("finding the area of the circle")
        to_find_area()
    
    elif choice==2:
        print("finding the circumference of the circle")
        to_find_circumference()

    else:
        print("error! invalid character! try again please type 1 or 2")

        print("the end thank you")
        


