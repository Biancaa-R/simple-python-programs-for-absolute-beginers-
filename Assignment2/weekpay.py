'''An employee’s total weekly pay equals the hourly wage multiplied by the total number of regular hours plus any overtime pay. Overtime pay equals the total overtime hours multiplied by 1.5 times the hourly wage. Write a program that takes as inputs the hourly wage, total regular hours, and total overtime hours and displays an employee’s total weekly pay. '''

hour_wage=float(input("Enter the hourly wage of the employee"))
reg_hours=float(input("enter the regular hours of the employee"))
ov_hours=float(input("enter the over hours of the employee"))

actual_pay=reg_hours*hour_wage
bonus=ov_hours*1.5*hour_wage

total=actual_pay+bonus

print("The employee worked for ",reg_hours+ov_hours, "hours")
print("The final pay of the employee is",total)
