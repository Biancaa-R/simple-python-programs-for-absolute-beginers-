from functools import reduce
l1=[1,2,3,4]
y=reduce(lambda x,y : x+y ,l1)
print(y)

from functools import reduce
y=reduce(lambda x,y : x*y ,l1)
print(y)


from functools import reduce
l1.remove(1)
y=reduce(lambda x,y : x**y,l1)
print(y)
