#program that determines and prints all the perfect numbers between 1 and 1000.


def perfect(n):
	_sum = 0
	for i in range(1, (n//2)+1):
		if n%i == 0:
			_sum += i
	if _sum == n:
		print(n)

for i in range(1, 1001):
	perfect(i)
