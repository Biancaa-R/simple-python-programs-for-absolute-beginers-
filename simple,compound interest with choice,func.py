
#I know this one is so lame

print("this program helps the user to find the simple interest and compound interest of a given principal ammount")

def simple():
    print(" to find simple interest")
    principal=float(input("enter the principal amount borrowed : "))
    rate_of_interest=float(input("enter the rate of interest :"))
    number_of_years=int(input("enter the number of years :"))
    simple_interest=principal*rate_of_interest*number_of_years/100
    ammount1=simple_interest+principal
    print("The value of ammount payable is",ammount1)
    print("the value of simple interest is",simple_interest)
    
def compound():
    print(" to find compound interest")
    principal=float(input("enter the principal amount borrowed : "))
    rate_of_interest=float(input("enter the rate of interest :"))
    number_of_years=int(input("enter the number of years :"))
    ammount2= principal*(1+rate_of_interest/100)**number_of_years
    compound_interest=ammount2-principal
    print("The value of ammount payable is",ammount2)
    print("the value of compound interest is ",compound_interest)
    

def main():
    print("do you want to find simple interest or compound interest")
    choice =str(input("type simple to find simple interest or compound to find compound interest"))


    if choice in ['simple','Simple']:
        simple()
        print("do you want to try again?")
        option2=str(input("type again if you want to try again.If you want to quit type quit"))

        if option2 in ['again','Again']:
            main()
        else:
            print("the end thank you")

    elif choice in ['compound','Compound']:
        compound()
        print("do you want to try again?")
        option3=str(input("type again if you want to try again.If you want to quit type quit"))

        if option3 in ['again','Again']:
            main()
        else:
            print("the end thank you")
    
    else:
       print(" you have entered an invalid option")
       print("do you want to try again?")
       option1=str(input("type again if you want to try again. If you want to quit type quit"))

       if option1 in ['again','Again']:
           main()
       else:
           print("the end thank you")
           print("program over")


main()

