#Find the transpose of a given matrix using list comprehension


rows=int(input("Enter the number of rows of matriceA"))
coloumns=int(input("Enter the number of coloumns of matriceA"))


row1=[]
matriceA=[]

for i in range(0,rows):
	for j in range(0,coloumns):
		x=int(input("Enter the element"))
                row1.append(x)
	matriceA.append(row1)
        row1=[]

print("matrice a inputted")

matriceB=matriceA

Y=[[matriceA[i][j] for j in range(0,coloumns)]for i in range(0,rows)]

print(Y)
