#Use the simultaneous assignment to get two points of x,y coordinates and calculate the slope(m) and constant© for the line equation(y=mx+c).

y1,y2=int(input("Enter the y1 value")),int(input("Enter the y2 value"))
x1,x2=int(input("Enter the x1 value")),int(input("Enter the x2 value"))

#y=mx+c
m,c=(y2-y1)/(x2-x1),  y1- ((y2-y1)/(x2-x1))*x1
print(c)
