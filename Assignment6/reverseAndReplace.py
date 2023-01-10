#program for reversing a string, then replace the occurrence of vowels with “$”.

def reverse(string):
	rev = ''
	for i in range(len(string)-1, -1, -1):#accessing the string from reverse
		rev += string[i]
	print("The string after reversing:", rev)
	replace(rev)

def replace(string):
	res=''
	for i in range(len(string)):
		if string[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']: #chekcing whether current character is vowel
			res+='$'
		else:
			res+=string[i]
	print("The string after repalcement:", res)



string = input("Enter a string: ")

reverse(string)
