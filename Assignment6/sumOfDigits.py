#program to get the sum of a non-negative integer

def sumDigits(n):
	if n == 0:
		return 0
	last = n%10
	return last + sumDigits(n//10)

n = int(input("Enter a number: "))

res = sumDigits(n)

print("The sum of the digits of the given number is", res)

