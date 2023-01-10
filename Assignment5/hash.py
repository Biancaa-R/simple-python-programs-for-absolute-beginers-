#Python program to replace each character of a word of length 5 and more with a hash character

string=input("Enter the string")
if len(string)<5:
	print(string)
else:
	print("#"*len(string))
