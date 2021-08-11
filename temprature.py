# A program to convert temprature from one system to another

print("type 1 to convert celsius temprature to farenheit")
print("type 2 to convert farenheit temprature to celsius")
print("type 3 to convert celsius temrature to kelvin")
print("type 4 to convert kelvin temprature to celsius")
print("type 5 to convert farenheit temprature to kelvin")
print("type 6 to convert kelvin temprature to farenheit")


choice=int(input("enter your choice 1,2,3,4,5 or 6  "))

if choice==1:
    print("aim: to convert celsius temprature to farenheit")
    celsius=float(input("enter the value of celsius temprature : "))
    farenheit=celsius*9/5+32
    float(farenheit)
    print("the celsius value of the temprature is ",celsius)
    print("the farenheit value of the temprature is ",farenheit)
    
elif choice==2:
    print("aim: to convert farenheit temprature to celsius")
    farenheit=float(input("enter the value of farenheit temprature: "))
    celsius=(farenheit-32)*5/9
    float(celsius)
    print("the farenheit value of the temprature is ",farenheit)
    print("the celsius value of temprature is ",celsius)

elif choice==3:
    print("aim: to convert celsius temprature to kelvin")
    celsius=float(input("enter the value of celsius temprature: "))
    kelvin=celsius+ 273.16
    float(kelvin)
    print("the celsius value of temprature is ",celsius)
    print("the kelvin value of temprature is ",kelvin)
    
elif choice==4:
    print("aim: to convert kelvin temprature to celsius")
    kelvin=float(input("enter the value of kelvin temprature: "))
    celsius=kelvin-273.16
    float(celsius)
    print("the kelvin value of temprature is ",kelvin)
    print("the celsius value of temprature is ",celsius)

elif choice==5:
    print("aim: to convert farenheit temprature to kelvin")
    farenheit=float(input("enter the value of farenheit temprature: "))
    celsius=(farenheit-32)*5/9
    float(celsius)
    kelvin=celsius+273.16
    float(kelvin)
    print("the farenheit value of temprature is ",farenheit)
    print("the kelvin value of temprature is ",kelvin)
    
elif choice==6:
    print("aim: to convert kelvin temprature to farenheit")
    kelvin=float(input("enter the value of kelvin temprature: "))
    celsius=kelvin-273.16
    float(celsius)
    farenheit=celsius*9/5+32
    float(farenheit)
    print("the kelvin value of the temprature is: ",kelvin)
    print("the farenheit value of temprature is: ",farenheit)
    
else:
    print("invalid choice")
    print("please enter a number in the set (1,2,3,4,5,6)")
    print("please try once again")

print("the end thankyou")
#the end of the program


























