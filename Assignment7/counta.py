'''Write a Python program that prompts the user to enter a list of  names and stores them in a list. The program should display how many times the letter 'a' appears within the list.'''

list1=[]
count=0
n=int(input("enter the number of elements in a list"))
for i in range(0,n):
	x=input("enter the name")
        list1.append(x)

for i in range(0,len(list1)):
 	count+=list1[i].count("a")

print(count)
