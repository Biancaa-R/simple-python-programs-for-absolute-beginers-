#Write a python program to check whether the given integer is a multiple of 5

value=int(input("Enter the number"))
if value%5==0:
    if value==5:
        print("The number is 5")
    else:
        print("The number is a multiple of 5")
else:
    print("The number is not a multiple of 5")
