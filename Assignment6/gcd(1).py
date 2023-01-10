# program to find gcd using recursion


def gcd(a, b): #assumed where a is greater than b
	if b == 0:
		return a
	
	return gcd(b, a%b)


a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if a > b:
	res = gcd(a, b)
else:
	res = gcd(b, a)

print("The gcd of given number is", res)
