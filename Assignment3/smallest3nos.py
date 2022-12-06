#Assignment3 3.Smallest of 3 numbers
a=int(input('Enter 1st no.:'))
b=int(input('Enter 2nd no.:'))
c=int(input('Enter 3rd no.:'))
m=a
if m<b and m<c:
    m=a
elif m<a and m<c:
    m=b
else:
    m=c
print('The smallest number is:',m)