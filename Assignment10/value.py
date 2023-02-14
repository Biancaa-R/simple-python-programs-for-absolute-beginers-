#1.Write a Python code to read the content of ‘ebook.txt’ and display the contents of the file onto the console.

F=open("ebook.txt","r")
value=F.read()
print(value)
F.close()
