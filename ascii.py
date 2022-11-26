'''Write a Python program that prompts the user to enter an upper or lower case letter and displays the corresponding Unicode encoding. '''

def unitlen():
    lower=input("Enter a lower case character")
    if len(lower)!=1:
        print("Enter exactly one character, valid ")
        unitlen()
    else:
        lower=lower.lower()
        value=ord(lower)
        print("The ascii value of the character is",value)


def unitlen1():
    upper=input("Enter a upper case character")
    if len(lower)!=1:
        print("Enter exactly one character, valid ")
        unitlen1()
    else:
        upper=upper.upper()
        value=ord(upper)
        print("The ascii value of the character is",value)

unitlen()
unitlen1()


