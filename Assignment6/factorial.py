#program to find factorial recursively


def fact(n):
	if n < 0:
		print("Can't find factorial for negatives")
		return -1

	if n <= 1:
		return 1
	
	return n * fact(n-1)


n = int(input("Enter the number: "))

res = fact(n)

if res != -1:
	print("The factorial of the given number is ", res)
