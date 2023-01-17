def perfect(num):
       	sum=0
	for i in range(1,num//2+1):
		if num%i==0:
			sum+=i
	if sum==num:
		return True
	else:	
		return False

num=int(input("Enter the number"))
x=perfect(num)
if x is True:
	print("It is a perfect number")
else:
	print("It is not a perfect number")
    
