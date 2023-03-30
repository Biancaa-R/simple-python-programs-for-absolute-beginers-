sum=0
l1=[]
def rem(num1):

    if num1<=0:
       return num1
    else:
        for i in l1:
            
            if (num1-i)<0:
                l1.remove(i)
        num2=num1
        num1=num1-l1[-1]

        for i in l2:
            if i==l1[-1]:
                return l2[i+1]+ rem(num2-l1[-1])
        
     
def fib(num):
    global x
    global l2
    x=0
    n1=-1
    n2=1
    n3=0
    while n3!=num:
        prev=n3
        n3=n1+n2
        n1=n2
        n2=n3
        x+=1
        new=n3
        l1.append(n3)
        

        if prev<num and new>num and prev!=new:
            
            l2=l1.copy()
            y=rem(num)
            print(y)
            break
    else:
        normal(x)
            
def normal(x):
    n1=-1
    n2=1
    n3=0
    for i in range(0,x+1):
        n3=n1+n2
        n1=n2
        n2=n3
    print(n3)  
    
    

n=int(input("Enter the number"))
fib(n)

