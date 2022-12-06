#Assignment3 5.alculate salary with bonus based on conditions
s=int(input('Enter salary:'))
g=input('Enter gender (F/M):')
sal=s
if s<10000:
    sal+=2/100*sal
if g.upper()=='F':
    sal+=15/100*s
elif g.upper()=='M':
    sal+=5/100*s
print('Total salary:',sal)