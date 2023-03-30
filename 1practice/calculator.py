#Python program to create a calculator:
import sys
n=len(sys.argv)
print(n,"arguments are passed")
print(sys.argv[0],"is the name of the file")
x=float(sys.argv[1])
y=float(sys.argv[2])
z=sys.argv[3]

result=0
if z=="+":
    result=x+y
if z=="-":
    result=x-y
if z=="*":
    result=x*y
if z=="/":
    result=x/y
if z=="%":
    result=x%y
if z=="//":
    result=x//y
else:
    print("Invalid argument")
print("The result is",result)
