#Practice:
#Fibonacci series:

'''def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1)+fib(n-2))

m=int(input("Enter the number of terms"))
for i in range(0,m):

    y=fib(i)
    print(y)

#Setting a number to power:
x=int(input("Enter the number"))
n=int(input("Enter the power"))

def power(x,n):
    if n==1:
        return x
    if n<=0:
        return 1
    else:
        return x* power(x,n-1)
for i in range(0,n+1):
    y=power(x,i)
    print(y)

#Sum of n natural numbers;
n=int(input("Enter the n value"))
def sum_n(n):
    if n<=0:
        return 0
    else:
        return n+sum_n(n-1)
y=sum_n(n)
print(y)

#Sum of even and odd numbers:
def sum_of_i(n):
    if n<=0:
        return 0
    else:
        return n+sum_of_i(n-2)
n=int(input("Enter a number"))
if n%2!=0:
    y=sum_of_i(n)
    x=sum_of_i(n-1)
    print(y,"Is the sum of odd numbers")
    print(x,"is the sum of even numbers")

else:
    y=sum_of_i(n)
    x=sum_of_i(n-1)
    print(x,"Is the sum of odd numbers")
    print(y,"is the sum of even numbers")'''

#String reversal

string=input("Enter the string to be reversed")
def reversal(string1):
    global string
    string=string1
    
    if len(string)==0:
        return string
    else:
        n=len(string)-1
        
        return string[-1]+reversal(string[0:n])
print(reversal(string))
#The length of string remains 4

#String reversal 2

string=input("Enter the string to be reversed")
def reversal(string):
    if len(string)==0:
        return string
    else:
        return reversal(string[1:])+string[0]
print(reversal(string))
    
