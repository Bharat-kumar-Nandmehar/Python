#STRING SLICING
print("1=If you want to print in order")
print("2=If you want to print in reverse")
ch=int(input("Enter your choice:"))
if ch==1:
     a=input("Enter the str:")
     c=int(input("Enter the number:"))
     print(a[0:c])
elif ch==2:
     a=input("Enter the str:")
     c=int(input("Enter the number:"))
     print(a[-1:-c-1:-1])
