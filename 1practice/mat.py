#Matrice input:
matrice=[]
row=[]
rows=int(input("Enter the number of rows in the matrice"))
coloumn=int(input("Enter the number of coloumns in the matrice"))
for i in range(0,rows):
    for j in range(0,coloumn):
        x=int(input("Enter the element"))
        row.append(x)
    matrice.append(row)
    row=[]
    print(" ")
#print(matrice)

matrice1=[]
row=[]
rows=int(input("Enter the number of rows in the matrice"))
coloumn=int(input("Enter the number of coloumns in the matrice"))
for i in range(0,rows):
    for j in range(0,coloumn):
        x=int(input("Enter the element"))
        row.append(x)
    matrice1.append(row)
    row=[]
    print(" ")
#print(matrice1)

#Matrice addition:
result=[]
for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        row.append(0)
    result.append(row)
    row=[]

for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        result[i][j]=matrice1[i][j]+matrice[i][j]
print(result)

#Transpose:
result1=[]
for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        row.append(0)
    result1.append(row)
    row=[]
    
for i in range(0,len(matrice)):
    for j in range(0,len(matrice[0])):
        result1[i][j]=result[j][i]
        
print(result1)

#Matrice multiplication:

A=matrice
B=matrice1

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j]+=A[i][k]*B[k][j]
