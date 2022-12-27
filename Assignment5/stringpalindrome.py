#Assignment 5
# string is palindrome or not
a=input('Enter string:')
if a==a[::-1]:
    print("String is a palindrome")
else:
    print('Not palindrome')