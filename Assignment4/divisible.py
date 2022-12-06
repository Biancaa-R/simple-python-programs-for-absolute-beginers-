#Print all the two digit numbers which are either divisible by 3 or by 4

for i in range(10,100):
    if i%3==0:
        print(i,sep=" ")
    else:
        if i%4==0:
            print(i,sep=" ")


