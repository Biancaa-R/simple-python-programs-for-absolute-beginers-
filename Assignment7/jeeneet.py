'''6.Create a list with “n” students name who have passed in JEE. Create another list with “m” students name who have passed NEET exams. Perform the following operations:a. Find the list of students who have qualified in both the exams.b. Print the students who have passed only in JEE as new list.c. Print the students who have passed only in NEET as new list.d. Print the students who have attended at least one exam.'''

n=int(input("Enter the number of students who cleared jee exam"))
m=int(input("Enter the number of students who cleared neet exam"))
jee=[]
neet=[]
intersection=[]
union1=[]
union=[]
onlyjee=[]
onlyneet=[]
for i in range(1,n+1):
    x=input("enter the name of the ",i,"th student who cleared jee")
    jee.append(x)

for i in range(1,m+1):
    x=input("enter the name of the ",i,"th student who cleared neet")
    neet.append(x)

for i in jee:
	if i in neet:
		intersection.append(i)
	else:
		onlyjee.append(i)

for i in neet:
	if i not in jee:
		onlyneet.append(i)
union=neet+jee

for i in union:
	if i not in union1:
		union1.append(i)
	
print(jee,"is the no. of people who took the jee exam")
print(neet,"is the number of people who took the neet exam")
print(intersection ,"is the number of people who took both the exams")
print(onlyjee,"is the no. of people who took the jee exam only")
print(onlyneet,"is the number of people who took the neet exam only")
print(union1,"is the total no.of candidates")


