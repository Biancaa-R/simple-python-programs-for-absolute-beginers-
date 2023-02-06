'''4. Write a Python program to create a list of tuples having first element as the
number and second element as the cube of the number.'''

n=int(input("Enter the number of terms"))
list1=[]
for i in range(0,n):
    x=int(input("Enter the number "))
    list1.append((x,x*3))

print(list1)    
    
