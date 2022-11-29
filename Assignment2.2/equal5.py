#Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

value1 =int(input("Enter the first number"))
value2 =int(input("Enter the second number"))

def boolean(value1,value2):
    if value1==value2:
        return True
    elif value1+value2==5:
        return True
    elif value1-value2==5 or value1-value2==-5:
        return True
    else:
        return False

print(boolean(value1.value2))
    

