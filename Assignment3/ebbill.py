#Assignment3 6.EB Bill
import math
p=float(input('Enter previous month reading:'))
c=float(input('Enter current month reading:'))
u=abs(p-c)
final=0
if u<500:
    final=u*1.5
elif u>1000:
    final=u*5
else:
    final=u*3
print('The toal amount to be paid is:',final)
