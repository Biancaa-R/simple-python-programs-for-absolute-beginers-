#4.Perform the division operation and find the quotient and remainder values. (Withoutusing /, // % operators)

divident=int(input("Enter the divident"))
divisor=int(input("Enter the divisor"))
quotient=0


while divident> divisor:
    divident=divident-divisor
    quotient+=1

print("quotient is",quotient)
print("The reminder is ",divident)
