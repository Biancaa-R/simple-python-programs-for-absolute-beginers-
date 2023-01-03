"""(Find the highest score) Write a program that prompts the user to enter the number
of students and each student’s score and displays the highest score and second
highest score."""

num=int(input("Enter the number of students"))
y=int(input("Enter the mark of the student"))
mini=y
maxi=y
for i in range(num-1):
    x=int(input("Enter the mark of the student"))
    if x<mini:
        mini=x
    elif x>maxi:
        sec=maxi
        maxi=x
    if x>sec and maxi>x:
        sec=x
        
print(mini,"is the least score")
print(maxi,"is the maximum score")
print(sec,"is the second highest score")
