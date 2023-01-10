#program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).

def _sum(n, x=0):
	if n-(2*x) <= 0: #base case where the element become 0 or negativeS
		return 0
	
	return n-(2*x) + _sum(n, x+1)

n = int(input("Enter the value of n: "))

res = _sum(n)

print("The sum of the series is", res)
