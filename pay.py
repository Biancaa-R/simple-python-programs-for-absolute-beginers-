'''Write a program to find the net salary of an employee by getting the basic pay (BP) as input. Compute the net pay based  upon the following formulae:DA = 88% of BP               HRA = 8% of BP CCA = Rs. 1000 Insurance = Rs. 2000 PF = 10% of BP Gross Pay = BP + DA + HRA + CCA Deductions = Insurance + PF '''

#Program to calculate the net salary of a person
bp=float(input("Enterthe basic pay of the employee"))
da=88/100*bp
hra=8/100*bp
cca = 1000 
Insurance =2000
pf=10/100*bp
GrossPay = bp+da+hra+cca
print("The gross pay of the employee is",GrossPay)
Deductions = Insurance + pf
print("The deductions of the employee is",Deductions)
print("The netsalary is",GrossPay-Deductions)

#end
