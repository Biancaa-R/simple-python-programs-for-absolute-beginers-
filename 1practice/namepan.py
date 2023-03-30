#Write   a   program   that   takes   user’s   name   and   PAN   card   number.   Validate   theinformation using string functions

#The first five characters are letters (in uppercase by default), followed by four numerals, and the last (tenth) character is a letter.

name=input("Enter your name")
if name.isalpha():
    print("You have entered a valid name")
else:
    print("you have written an invalid name")

string=input("Enter your pan id")
if len(string)==10:
    for i in range(0,5):
        if string[i].isalpha():
            pass
        else:
            print("You have entered an invalid pan")
            break
        for i in range(5,8):
            if string[i] in "0123456789":
                pass
            else:
                print("you have entered an invalid pan")
                break
        for i in range(9,10):
            if string[9].isalpha():
                print("You have entered a valid pan")
                break
            else:
                print("You have entered an invalid pan")
                break
        break
else:
    print("You have entered an invalid pan")
        
