"""Write a Python program that prints all the numbers from 0 to 7 except 3 and 6.
Note: Use 'continue' statement"""

for i in range(0,8):
    if i==3 or i==6:
        continue
    print(i,end=" ")
