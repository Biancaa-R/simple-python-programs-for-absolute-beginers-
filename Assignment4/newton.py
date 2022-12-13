#Write a program to find the square root of a number using Newton’s method

num=int(input("Enter the number to find square root"))
approx=num
sq_root=1
while sq_root!=approx:
    approx=sq_root
    sq_root=(approx+num/approx)/2
print(sq_root)
