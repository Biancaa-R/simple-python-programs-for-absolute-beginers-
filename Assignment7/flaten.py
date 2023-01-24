'''.Obtain a nested list use looping constructs and list comprehension to flatten the list. Example: [[1],[2,3],[4,5,6],[7,8,9,10]]o/p: [1,2,3,4,5,6,7,8,9,10]'''

unflat=[[1],[2,3],[4,5,6],[7,8,9,10]]
flat=[i for j in unflat for i in j]
print(flat)
