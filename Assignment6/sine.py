#program to find sine series

def fact(i):
	if i == 0:
		return 1
	return i * fact(i-1)

def sine_series(x, c, n, i):
	if i == n:
		return 0
	else:
		if i % 2 == 0:
			return -(x ** c) / fact(c) + sine_series(x, c+2, n, i+1)
		else:
			return (x ** c) / fact(c) + sine_series(x, c+2, n, i+1)


x = float(input("Enter the angle in radians: "))
n = int(input("Enter the number of terms to appoximate: "))

print("The approx sine value is: ", sine_series(x, 1, n, 1))
