#To determine the first digit of a givn number
num=int(input("Enter the number"))
if num<0:
    num=num*-1
else:
    pass

while num>10:
    num=num//10

print("The first digit of the number is",num)
#end
