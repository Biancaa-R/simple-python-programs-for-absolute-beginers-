#Assignment3 5.alculate salary with bonus based on conditions
salary=int(input('Enter salary:'))
g=input('Enter gender (F/M):')
totsal=salary
if salary<10000:
    totsal+=2/100*salary
if g.upper()=='F':
    totsal+=15/100*salary
elif g.upper()=='M':
    totsal+=5/100*salary
print('Total salary:',totsal)
