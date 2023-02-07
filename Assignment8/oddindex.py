'''Consider a tuple as T = (1, 3, 2, 4, 6, 5). Write a program to store numbers present at odd index into a new tuple.'''

tup=eval(input("Enter the tuple of numbers"))
n=len(tup)
tup2=tuple()

for i in range(0,n):
	if i%2!=0:
		tup2+=(tup[i],)
print(tup2)
