#sum of odd or even using recursion:
num= int(input("Enter the number"))
def odd(num):
	if num==0:
        	return 0
	else:
		if num%2==1:
               		x=num
		else:
			x=0
		return x+odd(num-1)

def even(num):
	if num==0:
        	return 0
	else:
		if num%2==0:
               		x=num
		else:
			x=0
		return x+odd(num-1)


print(odd(num),"is the sum of odd numbers")
print(even(num),"is the sum of even numbers")             	 
		
