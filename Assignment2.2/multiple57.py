#Write a python program to check whether the given integer is a multiple of both 5 and 7
value=int(input("Enter the number"))
if value%5==0:
    if value%7==0:
        print("The number is a multiple of both 5 and 7")
    else:
        print("The number is a multiple of only 5")

elif value%7==0:
    print("The number is a multiple of only 7")
else:
    print("The number not a multiple of 5 and 7")

