#Assignment3 7.Comments based on marks
a=float(input('Enter mark 1:'))
b=float(input('Enter mark 2:'))
c=float(input('Enter mark 3:'))
d=float(input('Enter mark 4:'))
e=float(input('Enter mark 5:'))
t=a+b+c+d+e
d=int(input('Enter total denomination:'))
per=t/d*100
if per>=90:
    print('Distinction')
elif per>=80 and per<90:
    print('First class')
elif per>=70 and per<80:
    print('Second class')
if per>=60 and per<70:
    print('Third class')
if per<60:
    print('Fail'),