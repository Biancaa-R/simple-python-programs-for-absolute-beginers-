#5lines
num=int(input("Enter the number of lines of pattern"))
rows=1
fore=num

for i in range(0,num):
    for k in range(0,fore):
        print(" ",end="")
    for j in range(0,rows):
        print("*",end=" ")
    rows=rows+1
    fore=fore-1
    print("")

