''' 5.Create a dictionary for 6 employee details with empno as key, name, dob and net-pay as
list of values use appropriate dictionary methods:
a. Create a dictionary with the above information.
b. Insert a new employee details as the second employee
c. Delete the employee at the 4th position
d. Delete the last employee
e. Increment the salary of all employees by 5% '''

dict1={}
for i in range(0,6):
    empno=int(input("Enter the key"))
    name=input("Enter the name")
    pay=int(input("Enter the pay"))
    dob=input("Enter dob ")
    dict1[empno]=[name,pay,dob]
name2=input("Enter the second name")
dict1.update({2:name2})

y=dict1.pop(4)
print(y,"is the deleted record")

n=len(dict1)
y=dict1.pop(n)
print(y,"is the deleted record")

for i in dict1:
    dict1[i]=dict1[i]+5/100* dict1[i]

print(dict1)

    
