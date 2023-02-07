'''Write a python program to find the “good” and “bad” words in a given input and it can be string or a sentence.  A word is termed as  “GOOD”, when it doesn’t have any re-peated characters else  “ BAD”.  Example:  APPLE is a BAD word – character ‘P’ is repeated. Define a function <Find_Type> and store the results in a list if the input is a sentence. Sample Input and Output: Input:  Enter the String:  GOOD Output:  BAD Word Input:  Enter the String:  GOOD or BAD Output:  [BAD, GOOD, GOOD]'''

def find_type(l1,l2):
	for i in range(0,len(l1)):
		for j in l1[i]:
			if l1[i].count(j)>1:
					
				l2.append("bad")
				i=i+1
					


		l2.append("good")
	l2.pop()
				
			
			

	return l2

l2=[]

string=input("Enter the string")
l1=string.split(" ")

y=find_type(l1,l2)
print(y)

			

