'''1. Write a function Assign_grade(Lst) which reads the marks of a student from a list
and assigns a grade and display the grade based on the following conditions:
if Marks >=90 then grade A
if Marks >=80 && <90 then grade B
if Marks >65 && < 80 then grade C
if Marks > =40 && <=65 then grade D
if Marks <40 then grade F
Create the List of Marks of 5 Students in English Subject by getting the input
from the user'''

grades=[]

def Assign_grade(list):
    for i in list:
        if i>=90:
            grade="A"
            grades.append(grade)
        elif i>=80 and i<90:
            grade="B"
            grades.append(grade)
        elif i>65 and i<80:
            grade="C"
            grades.append(grade)
        elif i>=40 and i<=65:
            grade="D"
            grades.append(grade)
        else:
            grade="F"
            grades.append(grade)
    return grades

list1=eval(input("Enter the marks of the students in english subject"))
list1=list(list1)
grades=Assign_grade(list1)
for i in grades:
    print(i)
        
        
        
