#Compute Exponentiation (power of a number) without using ** operator

num=int(input("Enter the number"))
exp=int(input("Enter the exponent value"))

value=num
for i in (1,exp):
    value*=num

print(value)

