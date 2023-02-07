
'''Write a python program to display the number in words [Tuple]. Eg. 123 O/p: ("one", "two”, “three”)'''

n=int(input("Enter the number"))

rem=0
tup=tuple()

while n>0:
	rem=n%10
	n=n//10
	if rem ==0:
		tup+=("zero",)
	if rem==1:
		tup+=("one",)
	if rem==2:
		tup+=("two",)
	if rem==3:
		tup+=("three",)
	if rem==4:
		tup+=("four",)
	if rem==5:
		tup+=("five",)
	if rem==6:
		tup+=("six",)
	if rem==7:
		tup+=("seven",)
	if rem==8:
		tup+=("eight",)
	if rem==9:
		tup+=("nine",)
print(tup)

	
