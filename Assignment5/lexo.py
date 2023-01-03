#program to sort the elements of a string in lexographical order

string = list(input("Enter a string: "))

swap = True
while swap:
    swap=False
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] > string[j]:
                string[j], string[i] = string[i], string[j]
                swap=True
print(''.join(string))
