'''Fibbonaci series:15. Print the Fibonacci series up to N numbers.
Ex: Fibonacci Series = 0 1 1 2 3 5 8 13 21....'''


n=int(input("Enter the number of terms"))
n1=-1
n2=1
for i in range(0,n):

    n3=n1+n2 
    
    print(n3)
    n1=n2
    n2=n3
