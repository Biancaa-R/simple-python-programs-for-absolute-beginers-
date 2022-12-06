'''For children and dog lovers it is an interesting and frequently asked question how old their dog would be if it was not a dog, but a human being. To calculate this task, there are various scientific and pseudo-scientific approaches. An easy approach can be:  A one-year-old dog is roughly equivalent to a 14-year-old human being  A dog that is two years old corresponds in development to a 22 year old person.  Each additional dog year is equivalent to five human years. '''

age=int(input("Enter the age of your dog"))

def humanage():
    if age==1:
        return(14)
    if age==2:
        return(22)
    if age==0:
        return(0)
    else:
        return(22+ (age-2)*5)

print("The human age of your loving dog is",humanage(age))
