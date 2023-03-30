#program to Check whether a given number is a happy or sad number.

def sqrDigit(n):
	_sum = 0
	while n:
		last = n%10
		n//=10
		_sum += last*last
	return _sum

def happyOrSad(n):
	if n < 10:
		if n == 1:
			return True
		return False
	else:
		happyOrSad(sqrDigit(n))


n = int(input("Enter a number: "))
happy = happyOrSad(n)

if happy:
	print("Happy")
else:
	print("Sad")
