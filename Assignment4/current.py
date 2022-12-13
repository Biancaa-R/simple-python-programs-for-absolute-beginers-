"""Write a python program for the below mentioned scenario.Program will require a
input in voltage if it is 5 V, then it is active if less than 5V, it is CUTOFF ,if   greater
than 5V it is Breakdown .Your program will continue to ask for input voltage until
you enter a CUTOFF VOLTAGE. In addition, the program will terminate if there is a
Breakdown voltage as input."""

while True:
    value=int(input("enter the voltage value"))
    if value<5:
        print("cutoff")
        break
    elif value>5:
        print("Breakdown")
        break
    elif value==5:
        print("active")
