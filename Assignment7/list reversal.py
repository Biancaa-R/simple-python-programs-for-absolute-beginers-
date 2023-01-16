'''4. Write a function print_reverse(Lst) to reverse the elements of a list. Pass the list 
as parameter to a function which reverses the list without using slice operation. 
Print the reversed list in the main program. (Avoid using return statement in 
function)'''
list1=eval(input("enter the list"))
list1=list(list1)
def reverse(list1):
    list2=list1.copy()
    n=len(list1)
    for i in range(0,n):
        list1[i]=list2[n-1-i]

reverse(list1)
print(list1)
