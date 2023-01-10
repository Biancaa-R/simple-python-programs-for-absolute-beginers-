#code to separate the digit,check if the digit is prime or not

def prime(num):
    for i in range(2,num):
        if num/i==0:
            return False
            break
    return True
        
        

def separation(num):
    if num==0:
        return 0
    else:
        rem=num%10
        y = prime(rem)
    	if y is True:
            print(rem,"is prime")
    	else:
            print(rem",is composite")
    	return separation(num//10)


num=int(input("enter the number"))
separation(num)	
