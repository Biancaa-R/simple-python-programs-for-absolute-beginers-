#Assignment3 10.Leap year or not
y=int(input('Enter year in numerals:'))
if y%4==0:
    print('Leap year')
elif y%100==0:
    if y%400==0:
        print('Leap year')
else:
    print('Not a leap year')
