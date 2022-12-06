"""  Five Star Video rents new videos for $3.00 a night and oldies for $2.00 a night. Write a program that the clerks at Five Star Video can use to calculate the total charge for a customer’s video rentals. The program should prompt the user for the number of each type of video and output the total cost. """

new=int(input("Enter the number of new video rentals"))
old=int(input("Enter the number of old video rentals"))
total_charge= new*3+old*2

print("The total charge in dolars is",total_charge)

while True:
    choice=input("Do you want to add more rentals? y/n")
    if choice in ["n","N"]:
        break
    
    new1=int(input("Enter the number of new video rentals"))
    old1=int(input("Enter the number of old video rentals"))
    
    new=new+new1
    old=old+old1
    
    total_charge= new*3+old*2
    

    print("The total charge in dolars is",total_charge)

print("The end")
