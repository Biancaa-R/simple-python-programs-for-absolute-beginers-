''' 13.Get a number as input from user. Find if the number is even or odd, and then if it is even, whether it is divisible by 4 or not, and if it is odd, whether it is divisible by 3 or not. '''
num=int(input("Enter the number"))
if num%2==0:
    print("the number is even")
    if num%4==0:
        print("The number is divisible by 4")

else:
    print("The number is odd")
    if num%3==0:
        print("The number is divisible by 3")
