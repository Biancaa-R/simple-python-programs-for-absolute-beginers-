#To determine the last digit of a number

num=int(input("Enter a number"))
if num<0:
    num=num*-1
else:
    pass
last=num%10
print("The last digit of the number is",last)
