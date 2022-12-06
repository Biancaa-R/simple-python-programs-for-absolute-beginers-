#Assignment3 3.Smallest of 3 numbers
a=int(input('Enter 1st no.:'))
b=int(input('Enter 2nd no.:'))
c=int(input('Enter 3rd no.:'))
mini=a

if b<mini:
    mini=b
if c<mini:
    mini=c

print('The smallest number is:',mini)
