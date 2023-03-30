res=[[6, 8], [10, 12]]
res1=[[6, 10], [8, 12]]

#result=[[0,0],[0,0]]
result=[[res[i][j] + res1[i][j] for j in range(len(res[0]))] for i in range (len(res))]
print(result)

#To print the prime numbers in the range 0 to 20
y=[[False if i%j==0 and i!=j else True for j in range(2,20)]for i in range(0,20)]
print(y)
for i in range(0,20):
    if False in y[i]:
        print(i, "is composite")
    else:
        print(i,"is prime")

X=res
Y=res1
