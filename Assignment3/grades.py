#Assignment3 4.Calculate average and display grade
a=int(input('Enter mark1:'))
b=int(input('Enter mark2:'))
c=int(input('Enter mark3:'))
avg=(a+b+c)/3
if avg>=90 and avg<=100:
    print('Grade A')
elif avg>=80 and avg<=89:
    print('Grade B')
elif avg>=70 and avg<=79:
    print('Grade C')
elif avg>=60 and avg<=69:
    print('Grade D')
elif avg>=0 and avg<=59:
    print('Grade F')
