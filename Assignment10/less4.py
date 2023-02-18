"""Write a function ‘display_words()’ in python to read lines from a text file "ebook.txt", and
returns a list with words less than 4 characters """

def display_words():
    F=open("alltypes.txt","r")
    value=F.readlines()
    for i in value:
        i=i.split()
        for j in i:
            if len(j)<4:
                print(j)

    F.close()

display_words()
