#Find all of the numbers from 1–1000 that are divisible by 8

l=[i for i in range(1,10) if i%8==0]
print(l)

#Find all of the numbers from 1–1000 that have a 6 in them
l=[i for i in range(1,10) if "6" in str(i)]

print(l)

def six(i):
    while i>0:
        rem=i%10
        i=i//10
        if rem==6:
            return True
    return False

l=[i for i in range(0,10) if six(i)==True]
print(l)

#Count the number of spaces in a string (use string above)
x="Practice Problems to Drill List Comprehension in Your Head."
p=0
l=[True for i in x if i==" "]
print(len(l))

#Remove all of the vowels in a string (use string above)
x="Practice Problems to Drill List Comprehension in Your Head."
l=[i for i in x if i not in "aeiou"]
string=""
for i in l:
    string+=i
print(string)

#Find all of the words in a string that are less than 5 letters (use string above)
x="Practice Problems to Drill List Comprehension in Your Head."
l1=[i for i in x.split(" ") if len(i)<=5]
print(l1)

#Use a dictionary comprehension to count the length of each word in a sentence (use string above)
x="Practice Problems to Drill List Comprehension in Your Head."
y={i:len(i) for i in x.split(" ")}
print(y)


    

