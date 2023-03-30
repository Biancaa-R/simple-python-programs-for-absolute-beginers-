'''The names of students and a list of GPA’s of two semesters of each student are in the
dictionary data structure.
1. Write a function ‘CGPA_stud’ to calculate the CGPA of each student and return
the computed information as a new dictionary.
2. Write a function ‘display_names’ that stores the details based on the ascending
order of the student names
3. Write a function ‘display_grade’ that stores the details of the student based on
the descending order of the CGPA.
4. Display the first three toppers '''

d1={"anna":[4.0,3.98],"biancaa":[4.0,4.0],"Avanthika":[3.5,3.0],"Avighna":[2.3,3.3],"Shanmathi":[0.1,0.2]}
d2=dict()

def cgpa_stud():
    avg=0
    for i in d1:
     
        for j in d1[i]:
            avg+=j
        avg=avg/2
        cgpa=avg/4*10
        d2[i]=cgpa
        avg=0
    return d2
print(cgpa_stud())


