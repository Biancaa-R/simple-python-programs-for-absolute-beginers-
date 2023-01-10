#program to find sum of odd and even in a range

def find_sum_odd(n):
	_sum = 0
	for i in range(n+1):
		if i%2 == 1:
			_sum += i
	
	return _sum

def find_sum_even(n):
	_sum = 0
	for i in range(n+1):
		if i%2 == 0:
			_sum += i
	
	return _sum


n = int(input("Enter the value of N: "))

odd = find_sum_odd(n)
even = find_sum_even(n)

print("The sum of odd numbers in the range is", odd)
print("The sum of even numbers in the range is", even)
