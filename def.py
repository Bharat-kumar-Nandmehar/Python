#Def function

def percentage(s):
    p=s/500*100
    return (p)
a=int(input("Enter the marks:"))
b=int(input("Enter the marks:"))
c=int(input("Enter the marks:"))
d=int(input("Enter the marks:"))
e=int(input("Enter the marks:"))
s=a+b+c+d+e
percent=percentage(s)
print("The percentage is",percent)


#Replictaion
#***
#**
#*
def replication(r):
    for i in range(0, 4):
        print("*" * (r - i))
r = int(input("Enter the number:"))
rep=replication(r)
