#Find the sum of series:  a. 1 + x^2/2 + x^3/3 + ... x^n/n

x=int(input("Enter the value of x"))
n=int(input("Enter the value of n"))
sum=1
print("1",end=" + ")
for i in (2,n+1):
    print(x**i/i, end=" + ")
    sum+=x**i/i

print(sum)
