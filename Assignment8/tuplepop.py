'''5. Given list of tuples, remove all the tuples with length K.
Input : test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], K = 2
Output : [(4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
Input : test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], K = 3
Output : [(4, 5), (4, ), (1, ), (3, 4, 6, 7)]'''

input1=eval("Enter the list of tuples")
input1=list(input1)

n=int(input("Enter the length of the tuple"))

for i in len(input1):
    if len(input1[i])==n:
        input1.pop(i)
print(input1)
