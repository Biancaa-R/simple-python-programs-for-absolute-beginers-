'''9. Create two matrices and  perform the following actions:i)  Pass 2 matrices to a function called add_mat(m1,m2). Compute addition of2 matrices and return the resultant matrix. ii) Pass 2 matrices to a function called mul_mat(m1,m2). Compute multiplication of 2 matrices'''

#inputting 2 matrices:

rows=int(input("Enter the number of rows"))
coloumns=int(input("Enter the number of coloumns"))

row1=[]
matriceA=[]
matriceB=[]

#For matrice addition both the matrices should have same number of rows and coloumns

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


def summation(matriceA,matriceB):
	Result=[matriceA[i][j]+matriceB[i][j] for j in range len(matriceA[0]) for i in range len(matriceA)]
        return Result

print(summation(matriceA,matriceB))



