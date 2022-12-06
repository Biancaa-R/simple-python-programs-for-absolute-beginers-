#Python code for a senario:

choice=input("Is it raining tomorrow y/n?")
if choice in "yY":
    print("Tidy up the cellar and paint the walls")
    choice=input("Do you have extra spare time left y/n")
    if choice in "yY":
        print("Do tax declaration")
else:
    print("Go for swimming")
print("Go for cinema in the evening")
