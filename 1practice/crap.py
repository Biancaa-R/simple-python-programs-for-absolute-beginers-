def pointerFunc(input) :
    return ("aa"*input[2], input[0], input[1]) 
def functionToDoOperation(x,y,z) :
    return (x*y)*z 
t=['fsf',5, 90] 
print(functionToDoOperation(*pointerFunc((1,2,3))) )

def numbers():
    x=int(input("Enter the first number"))
    y=int(input("Enter the second number"))
    z=int(input("enter the third number"))
    if x==y==z:
        return 3*(x+y+z)
    else:
        return (x+y+z)

print("The output of the program is",numbers())

