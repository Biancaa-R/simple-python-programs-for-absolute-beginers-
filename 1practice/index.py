#Assignment 5
#3. Write a Python program to calculate the length of a string and to print the index of
#the character in a string without library function
l=0
a=input('Enter a string:')
for x in a:
    l+=1
print('length',l)
b=input('Enter the character whose index is to be found:')
for x in range(l):
    if a[x]==b:
        print(a[x],x)

       
