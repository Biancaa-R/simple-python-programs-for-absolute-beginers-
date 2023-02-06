'''8. Given a list of tuples, extract all tuples having K digit elements.
Input: test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )], K = 2
Output: [(34, 55), (12, 45), (78,)]
Explanation: All tuples have numbers with 2 digits.
Input: test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (782, )], K = 3
Output: [(782,)]
Explanation: All tuples have numbers with 3 digits.'''

l1=eval(input("Enter the list of tuples"))
l1=list(l1)
x=True

for i in l1:
    for j in i:
        if len(j)==n:
            pass
        else:
            break
            x=False

    if x==True:
        print(i)
