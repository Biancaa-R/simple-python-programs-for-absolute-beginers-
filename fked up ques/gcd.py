#Compute the GCD of two given numbers.
i=1
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))

if num1>num2:
    lower=num2
else:
    lower=num1 #works even if both the numbers are equal

while(i<=lower):
    if num1%i==0 and num2%i==0:
        gcd=i
    i+=1
print(gcd,"is the gcd of the 2 numbers")
if gcd==1:
    print("The numbers are coprime ")
    

