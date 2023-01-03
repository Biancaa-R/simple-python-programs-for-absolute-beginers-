#Write a python program that replaces all the vowels in the string with ‘*’

str=""
string=input("enter the string")
for i in range(len(string)):
    if string[i] in "aeiou":
        str+="*"
    else:
        str+=string[i]
print(str)
