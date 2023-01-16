'''2. Generate a list of 10 elements between 0 to 6 using random number generator.
Write a function rem_dup( glist) which gets the generated list as input and
remove the duplicates and return the updated list. '''

#list generation
list=[]
import random
for i in range(0,10):
    x=random.randint(0,6)
    list.append(x)
print(list)

l1=[]

def rem_dep(list):
    for i in list:
        if i in l1:
            continue
        else:
            l1.append(i)
    return l1

new=rem_dep(list)
print(new)
    
