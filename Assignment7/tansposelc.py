#Transpose using list comprehenson:

m = [[1,2],[3,4],[5,6]]
for row in m :
	print(row)

rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print("\n")
for row in rez:
	print(row)

matrix=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for row in matrix:
	print(row)
print("\n")

t_matrix = zip(*matrix)
for row in t_matrix:
	print(row)

