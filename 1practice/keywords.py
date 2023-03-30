"""Write a python code that reads a python code ‘code.txt’ and displays the python keywords
in the given file. """
keywords=["print","input","None","True","False","if","else","elif","def"]

F=open("code.txt.txt","r")
value=F.readlines()
for j in value:
    j=j.split()
    for i in j :
        if i in keywords:
            print(i)
F.close()
