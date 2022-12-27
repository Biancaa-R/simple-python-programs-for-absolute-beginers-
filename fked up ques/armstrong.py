'''Check whether the entered number is an Armstrong number or not. For
example: 153= 13 + 53 + 33 = 153 is an Armstrong number'''

num=int(input("Enter the number"))
temp=num
count=0
i=0
arm=0
while num>0:
    num=num//10
    count+=1
    
num=temp    
while i<count and num>0:
    rem=num%10
    arm+=rem**count
    num=num//10
    i=i+1

print(arm)    
if arm==temp:
    print("Yes it is an amstrong number")

else:
    print("No it is not an amstrong number")


