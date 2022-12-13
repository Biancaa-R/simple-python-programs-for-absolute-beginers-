#Check whether the given number is palindrome or not
num=int(input("Enter the number to check pallindrome"))
temp=num
digits=0
rev=0
while num>0:
    rem=num%10
    num=num//10
    digits+=1
    rev=rev*10+rem

if rev==temp:
    print("The number is a pallindrome")
else:
    print("The number is not a pallindrome")


