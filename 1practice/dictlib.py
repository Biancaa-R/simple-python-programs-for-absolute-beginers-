n=int(input("Enter the number of records"))
d1={}
for i in range(0,n):
    bid=int(input("Enter the book id of the book"))
    name=input("input the name of the book")
    author=input("enter the author name")
    copy=int(input("Enter the copies available"))
    d2={bid:(name,author,copy)}
    d1.update(d2)
for i in d1:
    print(i,d1[i])

choice =input("Enter the nme of the book")
for i in d1:
    if d1[i][0]==choice:
        if d1[i][2]>0:
            print("The book is available",d1[i][2],"copies are available")
        else:
            print("The book is not available")

choice=input("Enter the name of author")
for i in d1:
    if d1[i][1]==choice:
        print(d1[i])
