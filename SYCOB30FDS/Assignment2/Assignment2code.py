def accept(a):
    n=int(input(("enter no of students\n")))
    for i in range(n):
        print("enter marks for",i+1,"th student & ab if abscent")
        b=input("")
        a.append(b)
    if(a[i]!='ab'):
        a[i]=int(a[i])
    elif(a[i]=='ab'):
        a[i]=-1
    print("marks of all students are=",a)
    return a
 

def avg(a):
    c=0
    #a[i]=int(a[i])
    for i in range(len(a)):
        a[i]=int(a[i])
        if(a[i]==-1):
            pass
        else :
            c=c+a[i]
    d=c/len(a)
    return d

def highest(a):
    c=a[0]
    C=int(c)
    for i in range(len(a)):
        if(c<=a[i]):
            c=a[i]
    return c
def lowest(a):
    c=a[0]
    for i in range(len(a)):
        if(a[i]<=c):
            c=a[i]
    return c

def absent(a):
    c=0
    for i in range(len(a)):
        if(a[i]==-1):
            c=c+1
    return c
def highfreq(a):
    d=1
    for i in range(len(a)):
        c=0
        for j in range(len(a)):
            if(a[i]==a[j]):
                c=c+1
            if(c>d):
                d=c
                e=a[i]
    #e=int(e)
    print("Number with highest frequency is ",e," & it's frequency is",d)
    return 
def menu():
    fds=[]
    while(True):
        x=int(input("enter 1 for accept & display marks of fds \n enter 2 for taking average score of cls \n enter 3 to get highest & lowest scores of cls \n enter 4 to get no.of students who are absent for test \n enter 5 to display marks with highest frequency \n enter 6 to stop\n"))
        if(x==6):
            break
        elif(x==1):
            accept(fds)
        elif(x==2):
            print(avg(fds))
        elif(x==3):
            print("Highest score is",highest(fds)," & Lowest score is",lowest(fds))
        elif(x==4):
            print("Number of absent students is ",absent(fds))
        elif(x==5):
            highfreq(fds)
menu()

