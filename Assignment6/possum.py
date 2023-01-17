#python program to calculate the sum of positive integers

num=int(input("Enter the number"))

def possum(num):
	if num<=0:
		return 0
	else:
		return num+possom(num-2)
	
print(possom(num))
