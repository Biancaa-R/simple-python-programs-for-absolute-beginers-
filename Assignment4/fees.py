'''(Financial application: compute future tuition) Suppose that the tuition for a
university is $10,000 this year and increases 5% every year. Write a program that
computes the tuition in ten years and the total cost of four years’ worth of tuition
starting ten years from now.'''
sum=0
principal=10000
for i in range(0,14):
    sum+=(5/100*10000)

print("you have to pay",principal+sum)
