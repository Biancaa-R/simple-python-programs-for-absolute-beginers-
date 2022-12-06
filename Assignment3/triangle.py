#Assignment3 2.Triangle classification
a=int(input('Enter side 1 measurement:'))
b=int(input('Enter side 2 measurement:'))
c=int(input('Enter side 3 measurement:'))
if a==b==c:
    print('Equilateral triangle')
elif a==b or b==c or a==c:
    print('Isoceles triangle')
else:
    print('Scalene triangle')