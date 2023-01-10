#Write a Python program to parse an email id to print from which email server it wassent

email=input("enter the email id")
email=email.split(".")
print(email[-2],"is the email sever of the email id")
