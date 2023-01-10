# Write a Python program to delete all occurrences of a specified character in agiven string without using in built functions.

str=""
string=input("Enter the string")
sub=input("Enter the sub string")
for i in len(string):
    if sub==string[i]:
        continue
    else:
        str+=i
print(str)
