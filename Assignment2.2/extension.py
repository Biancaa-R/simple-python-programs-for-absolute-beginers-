#Write a python program to get filename with extensity on as user  input and display the extension alone.

file=input("Enter the name of the file with extension")
value=file.split(".")
print(value[-1])

