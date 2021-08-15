#Python program to remove the punctuation in a user entered string
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

string=input("Enter a string with punctuations>")

# remove punctuation marks from the string
newstring = ""
for char in string:
   if char not in punctuations:
       newstring+= char


print(newstring)
