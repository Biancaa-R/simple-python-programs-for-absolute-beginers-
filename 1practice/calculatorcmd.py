#Cmd calculator:

import sys

n=len(sys.argv)
print("There are ",n ,"arguments")
result=0
for i in range(0,n):
    print(sys.argv[i],"is the",i+1,"th argument")
print(sys.argv[0],"is the name of the program")
a=int(sys.argv[1])
b=int(sys.argv[2])
c=sys.argv[3]
if c=="+":
    result=a+b
if c=="-":
    result=a-b
if c=="*":
    result=a*b
if c=="/":
    result=a/b
if c=="%":
    result=a%b
print("The result is",result)
