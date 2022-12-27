'''Write a Python program to count the number of occurrences of a substring in agiven string and print the starting index of the substring for each occurrence. If thesubstring is not found in the given string return 'Not found'''
prev=0

sub=input("enter the substring")
string=input("enter the string")
if sub in string:
    count=string.count(sub)
    print(count,"no. of occurances")

    for i in range(0,len(string)):
        x=string.find(sub,i)
        if x==-1 :
            pass
        else:
            if x==prev and prev!=0:
                pass
            else:
                print(x)
                prev=x
else:
    print("not found")    
