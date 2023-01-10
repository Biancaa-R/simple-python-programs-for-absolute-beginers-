#Assignment 5
#menu driven
'''a. First occurrence of a substring from the end. 
 b. Right justify a string. 
 c. Capitalize the first letter of a string. 
 d. Check whether the string is alphanumeric. 
 e. Partition the given text into three parts
 f. end'''
print('a. First occurrence of a substring from the end. ','b. Right justify a string.',\
'c. Capitalize the first letter of a string.','d. Check whether the string is alphanumeric.',\
'e. Partition the given text into three parts''f.end',sep='\n')

while True:
    i=input('Enter option:')
    k=input('Enter string:')
    if i.lower()=='a':
        b=input('Enter substring:')
        print(k.index(b,-len(k),-1))
    elif i.lower()=='b':
        m=int(input('Enter number of spaces'))
        print(k.rjust(m))
    elif i.lower()=='c':
        print(k.capitalize())
    elif i.lower()=='d':
        if k.isalnum():
            print('Alphanumeric')
    elif i.lower()=='e':
        print(k.partition())
    elif i.lower()=='f':
        break
    else:
        print('Invalid input')