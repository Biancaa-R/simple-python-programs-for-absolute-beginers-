'''3. Write a Python program to combine two dictionary adding values for common keys.
d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
a. Infer the output of the new dictionary
b. Display only the keys of the new dictionary
c. Display only the values
d. Display the key_value pair'''
d3={}
d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}

for i in d1:
    if i in d2:
        if d1[i]==d2[i]:
            d3[i]=d1[i]

print(d3)

print(d3.keys())
print(d3.values())
print(d3.items())
