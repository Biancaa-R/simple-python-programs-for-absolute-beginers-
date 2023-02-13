test_list=eval(input("Enter the list of tuples"))
K=int(input("Enter the digit"))
List=[Tup for Tup in test_list if all(len(str(num))==K for num in Tup) ]
print(List)
