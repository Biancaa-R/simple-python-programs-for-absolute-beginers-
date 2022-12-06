#Write a Python program to get a single string separated by a space, from two given strings swap thefirst two characters of each string and display the result‘abc’ ‘xyz’   ‘xyc’ ‘abz’

strings=input("Enter two strings with space")
if " " not in strings:
    print("enter a valid string")

else:
    strings=strings.partition(" ")
    print(strings)
    string1=strings[0]
    string2=strings[2]
    string1,string2=string2[0]+string1[1:len(string1)+1],string1[0]+string2[1:len(string2)+1]
    print(string1,string2)

