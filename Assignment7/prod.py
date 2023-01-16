'''3. Create a list arr with “n” integers, construct a new list prod_list of same size 
such that prod_list[i] is equal to the product of all the elements of arr except 
arr[i].
Eg: l1=[1,2,3] where l1[0]==2*3, l1[1]=1*3 and l1[2]=1*3
Prod_list=[6,3,2]'''

list1=eval(input("Enter the list "))
list1=list(list1)
prod=[]
x=1
for i in range(0,len(list1)):
    for j in range(0,len(list1)):
        if i!=j:
            x*=list1[j]
    prod.append(x)
    x=1
print(prod)

        
