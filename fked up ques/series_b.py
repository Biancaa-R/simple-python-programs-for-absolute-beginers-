"""Print the sum of the series b. -x + x 2 – x 3 +x 4 +...."""
sum=0
x=int(input("Enter the value of x"))
n=int(input("Enter the value of n"))
for i in range(1,n+1):
    pre=((-1)**i)
    sum+=pre*(x**i)
print(sum)
