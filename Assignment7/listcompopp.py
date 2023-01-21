'''10. Give an appropriate list comprehension for each of the following:i)L1 = [1, ’x’, 4, 5.6, ’z’, 9, ‘a’, 0, 4] create a list which consists of integer values.ii)Producing a list of consonants that appear in string w.iii)Multiples of 10 (n values)iv)Construct a list of the form: [‘1a’,’2a’,’3a’,’4a’]v)Create a list which stores the sum of each of the elements from the two lists.'''

L1 = [1, ’x’, 4, 5.6, ’z’, 9, ‘a’, 0, 4] 
L2=[]
L3=[]
for i in L1:
	if type(i)==int:
	L2.append(i)
print(L2)

for i in L1:
	if i.isalpha():
		if i not in "aeiou":
			L3.append(i)
print(L3)

n=int(input("Enter the value of n"))

L=[10*i for i in range(1,n+1)]
print(L)

L=[str(i)+"a" for i in range(1,n+1)]
print(L)

L1=[1,2,3,4,5,6]
L2=[7,8,9,10,11,12]

L=list(map(lambda L1,L2 : L1+L2, L1,L2))

print(L)
