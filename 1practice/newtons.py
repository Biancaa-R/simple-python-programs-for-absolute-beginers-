#Newtons method of finding square root
num=int(input("Enter the number to find square root"))
approx=num
sqrt=1
while approx!=sqrt:
    approx=sqrt
    sqrt=(approx+num/approx)/2
else:
    print(sqrt)
