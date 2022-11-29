#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers

string=input("Enter a string of comma separated values")
string=string.split(",")
print(string, "is the list of comma separated values")
print(tuple(string) ,"is the tuple of comma separated values")
