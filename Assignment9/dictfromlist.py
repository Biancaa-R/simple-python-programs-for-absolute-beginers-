'''2.Create two lists storing the names of the persons in L1 and age of the corresponding person in L2 . Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value. '''

l1=[],l2=[]
dict1={}
n=int(input("Enter the number of records"))
for i in range(n):
	name=input("Enter the name of the student")
	age=int(input("Enter the age"))
        l1.append(name)
	l2.append(age)
for i in range(0, n):
	dict1[l1[i]]=l2[i]
print(dict1)
	
