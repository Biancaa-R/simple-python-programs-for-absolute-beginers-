def ackermann(m,n):
	if m==0:
		return n+1
	if m>0 and n==0:
		return ackermann(m-1,1)
	if m>0 and n>0:
		return ackermann(m-1, ackermann(m,n-1))
m=int(input("Enter the value of m"))
n=int(input("enter the value of n"))

print(ackermann(m,n))

