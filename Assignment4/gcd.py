#Compute the GCD of two given numbers.
i=1
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))

if num1>num2:
    lower=num2

elif num1==0 or num2==0:
    if num1==0:
        print("The gcd is",num2)
    if num2==0:
        print("the gcd is",num1)
else:
    lower=num1 #works even if both the numbers are equal

while(i<=lower):
    if num1%i==0 and num2%i==0:
        gcd=i
    i+=1
print(gcd,"is the gcd of the 2 numbers")
if gcd==1:
    print("The numbers are coprime ")
    

