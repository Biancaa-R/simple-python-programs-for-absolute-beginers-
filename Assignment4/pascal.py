#pyhon pattern programs:
fore=7
value=[1,]
ini=[1,1]
for i in range(2,9):
    for j in range(0,fore):
        print(" ",end="")
    if i==2 or i==3:
        for k in range(1,i):
            print("1",end=" ")
    else:
        
        for i in range(len(ini)-1):
            value.append(ini[i]+ini[i+1])
            value.append(1)
            for i in value:
                print(i,end=" ")
            ini=value
            value=[1,]

            
        
