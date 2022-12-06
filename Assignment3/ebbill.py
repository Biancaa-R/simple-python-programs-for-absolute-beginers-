#Assignment3 6.EB Bill
import math
p=float(input('Enter previous month reading:'))
c=float(input('Enter current month reading:'))
u=abs(p-c)
b=0
if u<500:
    b=u*1.5
elif u>1000:
    b=u*5
else:
    b=u*3
print('PLease pay:',b)