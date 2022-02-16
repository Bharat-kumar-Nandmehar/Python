#Menu driven programme
print("1 Sum of two numbers")
print("2 Product of two numbers")
print("3 Discrimanant ")
print("4 Table of number ")
ch=int(input("Enter your choice:"))
if (ch==1):
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    c=a+b
    print("The sum is:",c)
elif (ch==2):
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    c=a*b
    print("The product is:",c)
elif (ch==3):
      a=int(input("Enter the value of x square:"))
      b=int(input("Enter the value of x:"))
      C=int(input("Enter the value of constant:"))
      d=b*b-4*a*C
      if (d>0):
          print("The roots are real=",d)
      elif (d==0):
          print("The roots are same=",d)
      elif (d<0):
          print("The roots are imaginary=",d)
      else:
          print("No roots=",d)
elif (ch==4):
      a=int(input("Enter the number:"))
      for i in range(1,11):
            print(str(a) + "X" + str(i) + "=" + str(a*i))















