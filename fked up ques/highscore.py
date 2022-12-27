"""(Find the highest score) Write a program that prompts the user to enter the number
of students and each student’s score and displays the highest score and second
highest score."""

num=int(input("Enter the number of students"))
mini=int(input("Enter the mark of the student"))
for i in range(num-1):
    x=int(input("Enter the mark of the student"))
    if x<mini:
        mini=x
print(mini)
