#To calculate the binary value:
rev=""
rem=0

num1=int(input("Enter the value of the number"))
while num1>0:
    rem=num1%2
    #rev=rev*10+rem
    rev=str(rem)+rev
    num1=num1//2

print(rev)
