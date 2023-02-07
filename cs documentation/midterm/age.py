'''Write a python program to print the age of a person. Input is two dates and have to consider leap years also to calculate the age.   The output should contain, Years, Months and Days. Sample Input and Output Input: Birth Date: 01.02.1982 Today: 07.02.2023 Output: 41 Years, 7 Days Input: Birth Date: 21.05.1962 Today: 07.02.2023 Output: 60 Years, 8 Months and 18 Days'''

birthdate=input("Enter your birthdate separated by dots")
today=input("Enter today's date separated by dots")

birthdate=birthdate.split(".")
today=today.split(".")

day1=int(birthdate[0])
day2=int(today[0])

month1=int(birthdate[1])
month2=int(today[1])

year1=int(birthdate[2])
year2=int(today[2])

years=year2-year1-1

days=(12-month1)*30+(30-day1) + (month2-1)*30+day2

months=days//30
days=days%30

if months>12:
	years+=months//12
	months=months%12

for i in range(year1,year2+1):
	if i%4==0 and i%100!=0:
		days+=1
	if i%100==0 and i%400==0:
		days+=1
	else:
		days+=0

print("You are ",years,"years",months ," months",days," days old")
	




