#program to print prime digits

def separation(n):
	while n:
		last = n%10
		n//=10
		prime = prime_finder(last)
		if prime:
			
			print(last)
	

def prime_finder(digit):
	prime = True
	for i in range(2, (digit//2)+1):
		if digit%i == 0:
			prime = False
			break
	return prime


n = int(input("Enter a number: "))
separation(n)
