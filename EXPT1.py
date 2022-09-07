/*
In second year computer engineering class, group A student’s play cricket, group B 
students play badminton and group C students play football. 
Write a Python program using functions to compute following: -
a) List of students who play both cricket and badminton 
b) List of students who play either cricket or badminton but not both 
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.
(Note- While realizing the group, duplicate entries should be avoided, Do not use SET 
built-in functions)
*/











seComp=[] 
grpA=[]
grpB=[]
grpC=[]

n=int(input("Enter Total No. OF Students Who Play Game:"))

for i in range(0,n):
    stu_name=input("Enter Name Of Student:")
    seComp.append(stu_name)
print("List Of Total Students:"+str(seComp))


def get_cricket():
    c=int(input("Enter  No. OF Students Who Play Cricket:"))
    for i in range(0,c):
        c_stu=input("Enter Name Of Student:")
        grpA.append(c_stu)
    print("List Of Students play Cricket:"+str(grpA))

def get_badminton():
    b=int(input("Enter  No. OF Students Who Play Badminton:"))
    for i in range(0,b):
        b_stu=str(input("Enter Name Of Student:"))
        grpB.append(b_stu)
    print("List Of Student play Badminton:"+str(grpB))

def get_football():
    f=int(input("Enter  No. OF Students Who Play Football:"))
    for i in range(0,f):
        f_stu=input("Enter Name Of Student:")
        grpC.append(f_stu)
    print("List Of Student play Football:"+str(grpC))


get_cricket()
get_badminton()
get_football()

def intersection(l1,l2):
    l3=[]
    for val in l1:
        if val in l2:
            l3.append(val)
    return l3

def union(l1,l2):
    l3=l1.copy()
    for val in l2:
        if val not in l3:
            l3.append(val)
    return l3

def diff(l1,l2):
    l3=[]
    for val in l1:
        if val not in l2:
            l3.append(val)
    return l3

def taskA(grpA,grpB):
    return intersection(grpA,grpB)
def taskB(grpA,grpB):
    ls3=[]
    d1=diff(grpA,grpB)
    d2=diff(grpB,grpA)
    ls3.append(union(d1,d2))
    return ls3

def taskC(grpA,grpB,seComp):
    c=diff(seComp,union(grpA,grpB))
    return len(c)


def taskD(grpA,grpB,grpC):
    c=diff(intersection(grpA,grpC),grpB)
    return len(c)

flag=1
while(flag==1):

    print("1)List of students who play both cricket and badminton ")
    print("2)List of students who play either cricket or badminton but not both")
    print("3)Number of students who play neither cricket nor badminton")
    print("4)Number of students who play cricket and football but not badminton.")
    print("5)Exit")
    ch=int(input("Enter Your Choice:"))

    if(ch==1):
        print("List of students who play both cricket and badminton:",taskA(grpA,grpB))
        a = input("\n\nDo you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")
    elif(ch==2):
        print("List of students who play either cricket or badminton but not both:",taskB(grpA,grpB))
        a = input("\n\nDo you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")
    elif(ch==3):
        print("Number of students who play neither cricket nor badminton:",taskC(grpA,grpB,seComp))
        a = input("\n\nDo you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")
    elif(ch==4):
        print("Number of students who play cricket and football but not badminton:",taskD(grpA,grpB,grpC))
        a = input("\n\nDo you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")
    elif(ch==5):
        flag=0
        print("Thank You")
    else:
        print("Wrong Choice!")
        a=input("\n\nDo you want to continue (yes/no) :")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Thanks for using this program!")
