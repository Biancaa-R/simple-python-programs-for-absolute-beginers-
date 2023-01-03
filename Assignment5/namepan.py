#Write   a   program   that   takes   user’s   name   and   PAN   card   number.   Validate   theinformation using string functions

#The first five characters are letters (in uppercase by default), followed by four numerals, and the last (tenth) character is a letter.

name=input("Enter your name")
if name.isalpha():
    print("You have entered a valid name")
else:
    print("you have written an invalid name")

pan=input("Enter your pan id")
if len(pan)==10:
    for i in range(0,5):
        if string[i].isalpha():
            pass
        else:
            break
        for i in range(5,9):
            if string[i] in "0123456789":
                pass
            if string[9].isalpha():
                print("You have entered a valid pan")
            else:
                break

        
