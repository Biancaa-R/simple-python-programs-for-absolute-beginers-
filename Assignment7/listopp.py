'''7. Assume that the variable’ data’ refers to the list [5, 3, 7]. Write the expressions that perform the following tasks:a. Replace the value at position 0 in data with that value’s negation.b. Add the value 10 to the end of data.c. Insert the value 22 at position 2 in data.d. Remove the value at position 1 in data.e. Add the values in the list newData = [9,11,13] to the end of data.f. Locate the index of the value 7 in data, safely.g. Find the maximum element in the list.h. Find the sum of all elements in the list.i. Sort the values in data.'''

data=[5,3,7]
newdata=[9,11,13]
x=data[0]
data[0]=-1*(x)

data.append(10)

data.insert(2,22)

data.pop(1)

data.extend(newdata)

print(data.index(7),"is the index of 7")

print(max(data))

print(sum(data))

print(data.sort())



