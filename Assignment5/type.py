#Write a Python program to count Uppercase, Lowercase, special character andnumeric values in a given string.
upper,lower,special,num=0,0,0,0

string=input("Enter the string")
for i in range (len(string)):
    if string[i].isupper()==True:
        upper+=1
    elif string[i].islower()==True:
        lower+=1
    elif string[i] in "1234567890":
        num+=1
    else:
        special+=1

print("The number of upper characters are",upper)
print("The number of lower characters are",lower)
print("The number of special characters are",special)
print("The number of numeric characters are",num)
