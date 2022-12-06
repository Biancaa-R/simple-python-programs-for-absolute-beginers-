'''Write a series of Python statements that will read three strings from the user, and then print them in dictionary order. (Note: you can compare two strings using the relational operators).'''

string1=input("Enter the first string")
string2=input("Enter the second string")
string3=input("Enter the third string")

list1=[string1,string2,string3]
list1.sort()

print(list1)
print(list1[0] ,"is the first string")
print(list1[1], "is the second string")
print(list1[2],"is the third string")
