#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.

value=input("Enter the string")

new=value[0:2]+value[-2:]
print(new)
