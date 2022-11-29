#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn and display the pattern
'''   n        
  n n        
 n n n'''
sum=0
n=int(input("Enter a number "))
for i in range(0,n):
    for j in range(0,i):
        print(n,end=" ")
    print(" ")

for i in range(0,n):
    for j in range(0,i):
        sum+=n*10**j
    print(sum,end=" + ")
    sum=0

print("\n end")
