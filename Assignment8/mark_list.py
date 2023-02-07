'''3. Consider the mark_list=[('Rams',120,55,45,65,45,32), ('Vel',121,94,86,78,67,90), ('Siri',122,73,98,90,87,89)] which contains the name, register number and marks of corresponding student as list of tuples. Create a new tuple that assigns a grade based on the following conditions:if Marks >=90 then grade Aif Marks >=80 && <90 then grade Bif Marks >65 && < 80 then grade Cif Marks > =40 && <=65 then grade DOutput:[('Rams',120,Grades),(.....)]'''

mark_list=[]

n=int(input("Enter the number of records"))

for i in range(0,n):
	name=input("Enter the name")
	roll=int("enter the roll")
	mark1=("Enter marks")
	mark2=("Enter marks")
	mark3=("Enter marks")
	mark4=("Enter marks")
	mark5=("Enter marks")
	mark_list.append(name,roll,mark1,mark2,mark3,mark4,mark5)
	


