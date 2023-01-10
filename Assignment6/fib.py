# program to solve Fibonacci sequence using recursion

def fib(n):
	if n <= 1:
       		return n
	else:
       		return(fib(n-1) + fib(n-2))

n = int(input("Enter a number: "))

res = fib(n)

print("The value of", n, "th digit in Fibonacci sequence is", res)
