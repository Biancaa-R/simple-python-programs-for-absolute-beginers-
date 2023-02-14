'''.A file “t1.txt” contains alphanumeric characters. Open the file in suitable access mode such that user can able to write the content into file and then read it without closing the file. Write a program to write few more lines into file, read the file content, count  and display the total number of capital letters, small  letters and  numbers or digits in the file. '''

F=open("Alltypes.txt","r+")

n=int(input("Enter how many lines you want to type?"))
for i in range(0,n):
	value=input("Enter the contnt")
	F.write(value)


v=F.read()
print(v)

	


