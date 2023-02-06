#7. Write a python program to remove duplicates from tuple.

tup=eval(input("enter the tuple"))
tup2=()
for i in tup:
    if i not in tup2:
        tup2+=(i,)
    else:
        continue
print(tup2)
    
