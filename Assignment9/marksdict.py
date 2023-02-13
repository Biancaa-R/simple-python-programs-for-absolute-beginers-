'''7. Consider the student details are maintained using nested dictionary as follows:
{Reg no: {subcode: CAT1, CAT2, SAT}}
a. Create nested dictionary for three subjects
b. Display the information of a student given his register number
c. To display the marks of a student given his subject code
d. Update the details of the student given the register number '''

d1={2210329:{"UEN2176":(45,45,45),"UMA2176":(50,50,50),"UPH2176"(47,47,47)},2210502:{"UEN2176":(44,44,44),"UMA2176":(50,50,50),"UPH2176"(37,37,37)},"2210345":{"UEN2176":(35,35,35),"UMA2176":(40,40,40),"UPH2176"(47,47,47)}}
reg=int(input("Enter the register no. to view data"))
for i in d1:
    if i==reg:
        print(i,d1[i])

d2={}
reg=int(input("Enter the register no. to view data"))
code=input("Enter the subject code")
for i in d1:
    if i==reg:
        for j in reg[i]:
            if j in code:
                print reg[i][j]

ch=int(input("Do you want to update the details?  yes/no 1,2"))
if ch==1:
    reg=int(input("Enter the register no."))
    for i in range(0,3):
        code=input("Enter the subject code")
        c=int(input("Enter marks"))
        c1=int(input("Enter marks"))
        c2=int(input("Enter marks"))
        d2[code]=(c,c1,c2)
    d1[reg]=d2
        
    
    
    
