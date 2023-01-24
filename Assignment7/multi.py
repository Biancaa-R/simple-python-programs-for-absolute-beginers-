'''9. Create two matrices and  perform the following actions:i)  Pass 2 matrices to a function called add_mat(m1,m2). Compute addition of2 matrices and return the resultant matrix. ii) Pass 2 matrices to a function called mul_mat(m1,m2). Compute multiplication of 2 matrices'''

#inputting 2 matrices:

rows=int(input("Enter the number of rows of matriceA"))
coloumns=int(input("Enter the number of coloumns of matriceA"))
coloumns2=int(input("Enter the number of coloumns of matrice B"))

row1=[]
matriceA=[]
matriceB=[]

for i in range(0,rows):
	for j in range(0,coloumns):
		x=int(input("Enter the element"))
                row1.append(x)
	matriceA.append(row1)
        row1=[]

print("matrice a inputted")

for i in range(0,rows):
	for j in range(0,coloumns):
		x=int(input("Enter the element"))
                row1.append(x)
	matriceB.append(row1)
        row1=[]

print("matrice B inputted")

result=[[sum(a * b for a, b in zip(rows, coloumns2)) for coloumns2 in zip(*matriceB)] for rows in matriceA]

print(result)
 


