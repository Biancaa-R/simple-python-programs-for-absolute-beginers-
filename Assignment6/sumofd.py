#To find the sum  of digits of a number using recursion:
num=int(input("Enter the number"))

def lenofnum(num):
    rem=num%10
    if num==0:
        return 0
    else:
        return (rem+ lenofnum(num//10))

print(lenofnum(num))

