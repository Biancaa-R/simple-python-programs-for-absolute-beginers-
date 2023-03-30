"""A word processing software is expected to calculate the frequency of each word in given
file. Write the python function “Find_all()” that accepts the file name and returns a
dictionary with word frequency"""

def findall():
    F=open("happy.txt","r")
    value=F.readlines()
    for i in value:
        for j in i.split():
            list1
