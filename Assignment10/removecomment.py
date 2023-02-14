'''3.A file ‘code.txt’ contains Python code. Write a program that will read the contents of ‘code.txt’ and copies the content into another file ‘recordcode.txt’ excluding the comment statement.  '''

F=open("code.txt","r")
value=F.readlines()
F.close()
for i in value:
	if i[0]=="#"
	value.remove(i)
F=open("recordcode.txt","w")
F.write(value)
F.close()
