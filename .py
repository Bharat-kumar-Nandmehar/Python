#MODULUS OF TWO NUMBERS
a=int(input("Enter the first no.:"))
b=int(input("Enter the second no.:"))
c=a%b
print("The remainder is=",c)

#DISCRIMINAT OF NUMBERS
a=int(input("Enter the value of x square="))
b=int(input("Enter the value of x="))
c=int(input("Enter the value of constant="))
d=b*b-4*a*c
if (d>0):
    print("The roots are real=",d)
if (d==0):
    print("The roots are same=",d)
if (d<0):
    print("The roots are imaginary=",d)
else :
    print("No roots= ",d)




