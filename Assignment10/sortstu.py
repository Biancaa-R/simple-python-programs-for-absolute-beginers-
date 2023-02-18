"""A file ‘student.txt’ contains the names of the students in the first semester. Write a python
function ‘sort_studentname()’ that reads the data from ‘student.txt’ and stores names
alphabetically in a file ‘sortstudent.txt’ """

def sort_studentname():
    F=open("student.txt","r")
    list1=[]
    value=F.readlines()
    F.close()
    for i in value:
        i=i.split()
        list1.extend(i)
    list1.sort()
    F=open("sortstudent.txt","w")
    for i in list1:
        F.write(i)
    F.close()
    print("values added")
sort_studentname()
    
