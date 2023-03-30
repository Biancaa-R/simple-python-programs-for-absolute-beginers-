#program to find the value of Ackermann function

def ack(m, n):
	if m == 0:
		return n+1
	elif m > 0 and n == 0:
		return ack(m-1, 1)
	elif m > 0 and n > 0:
		return ack(m-1, ack(m, n-1))


m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

print("The value of Ackermann function for", m, "and", n, "is:", ack(m,n))
