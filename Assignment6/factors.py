# program to finds the factors of the given number and displays it


def factors(n=10):
	for i in range(1, (n//2)+1):
		if n%i == 0:
			print(i, "is a factor of", n)

choice = input("Want to give a number? (yes/no): ")

if choice == "yes":
	n = int(input("Enter a number: "))
	factors(n)
else:
	factors()

