#Write a python program that reads a sentence, where each word is separated by aspace. The program should replace each blank with a hyphen
string=input("Enter the string with spaces")
string2=""
for i in len(string):
	if string[i] is " ":
		string2+="-"
	else:
		string2+=string[i]
		
        
    

