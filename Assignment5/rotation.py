#String rotation:
i=int(input("Enter the amount of rotation"))
string=input("enter the string to be rotated")

alpha="abcdefghijklmnopqrstuvwxyz"
for j in string:
	if j in alpha:
		k=alpha.index(j)
		k=k+i
		if k>25:
			k=k-25
		print(alpha[k])
