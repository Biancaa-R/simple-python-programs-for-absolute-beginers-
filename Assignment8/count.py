'''6. Given a list, find frequency of each element and save it as list of tuple
[(number, frequency)].
Input : test_list = [4, 5, 4, 5, 6, 6, 5]
Output : [(4, 2), (5, 3), (6, 2)]
Input : test_list = [4, 5, 4, 5, 6, 6, 6]
Output : [(4, 2), (5, 3), (6, 3)]'''

x=int(input("Enter the length of the list"))
l1=[]
for i in range(x):
    y=int(input("enter the element"))
    l1.append(y)

list1=[]
for i in l1:
    count=l1.count(i)
    tup=(i,count)
    list1.append(tup)

print(list1)
    
    
    
