#ASsignment 5
#delete certain occurences from a string
a=input('Enter a string:')
b=input('Enter character to be deleted:')
s=''
for x in a:
    if x==b:
        continue
    else:
        s+=x
print(s)