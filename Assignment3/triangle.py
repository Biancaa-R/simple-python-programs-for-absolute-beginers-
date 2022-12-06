#Assignment3 2.Triangle classification based on the number of equal sides

a=int(input('Enter the side 1 measurement:'))
b=int(input('Enter the side 2 measurement:'))
c=int(input('Enter the side 3 measurement:'))
if a==b==c:
    print('The given triangle is an Equilateral triangle')
elif a==b or b==c or a==c:
    print('The given triangle is an Isoceles triangle')
else:
    print('The given triangle is an Scalene triangle')
