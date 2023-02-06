#Students pov:

def main():
    global marks
    global ques
    global name
    global value
    name=input("Enter your name")
    while len(value)>0:
        value=list(value)
        i=random.choice(range(0,len(value)))
        print(ques,value[i][0],value[i][1])
        ans=input("Enter the answer")
        
        if ans==value[i][2][0]:
            marks+=4
            ques+=1
        else:
            marks-=1
            ques+=1
        value.pop(i)

    
    print("You have completed the quiz")
    print(name,marks, ques,"Questions attempted")

    F=open("high_scores.dat","rb")
    record=pickle.load(F)
    record.append([name,marks])
    for i in record:
        record.sort(key=lambda record : record [0][1])
    F.close()

    F=open("high_scores.dat","wb")
    pickle.dump(record,F)
    F.close()

def add_ques():
        F=open("quiz.dat","rb")
        value=pickle.load(F)
        n=int(input("How many questions do you want to enter?"))
        for i in range(n):
            que=input("Enter the question")
            opt=input("enter the options")
            ans=input("enter the answer")
            value.append([[que],[opt],[ans]])
        F.close()
        F=open("quiz.dat","wb")
        pickle.dump(value,F)
        print("Questions added successfully")
        F.close()

import random
import pickle
F=open("quiz.dat","rb")
value=pickle.load(F)
#value=value.split("-")
n=len(value)
print("there are ",n ,"questions")
F.close()

marks=0
ques=0

ch=input("Are you the quiz master or the student q/s")

while True and ch in "sS":
    choice=input("do you want to Start quiz? yes/no \n view high scores? h")
    if choice in ["yes","Yes"]:
        main()
    elif choice in ["h","H"]:
        F=open("high_scores.dat","rb")
        value=pickle.load(F)
        print(value)
        F.close()

    else:
        break

while True and ch in "qQ":
    choice=input("Do you want to add more questions? add /view high scores? h or view questions? v")
    if choice in ["h","H"]:
        F=open("high_scores.dat","rb")
        value=pickle.load(F)
        print(value)
        F.close()
    elif choice in ["add","Add"]:
        add_ques()

    elif choice=="v":
        F=open("quiz.dat","rb")
        value=pickle.load(F)
        print(value)

    
    else:
        break
        
        



        
    
    
    
