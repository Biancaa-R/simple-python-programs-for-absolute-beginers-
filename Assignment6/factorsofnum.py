#To print the factors of a number

def factors(num):
	for i in range(1,num):
		if num%i==0:
			print(i,"is the factor of the number",num)
 	
num=int(input("enter the number "))

factors(num)

