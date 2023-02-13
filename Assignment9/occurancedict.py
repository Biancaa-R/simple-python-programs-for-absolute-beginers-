'''8. Write a function that creates and return a dictionary which finds the frequency of
occurrence of the characters by obtaining the input string from the user. '''
dict1={}
x=input("Enter a string")
for i in x:
    v=x.count(i)
    dict1[i]=v
print(dict1)
