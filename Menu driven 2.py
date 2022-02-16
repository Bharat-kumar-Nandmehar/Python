#Menu driven
print("1 Convert celcius to fahrenheit ")
print("2 Percentage of the marks ")
print("3 Average of marks")
print("4 Convert word(The) into (A)")
ch=int(input("Enter your choice:"))
if (ch==1):
    a=int(input("Enter the Temperature (Celcius):"))
    b=a*9/5+32
    print("The Fahrenheit=",b)
elif (ch==2):
    c=float(input("Enter the marks in Chemistry:"))
    p= float(input("Enter the marks in Physics:"))
    m= float(input("Enter the marks in Maths:"))
    e= float(input("Enter the marks in English:"))
    cs = float(input("Enter the marks in Computer Science:"))
    Total=c+p+m+e+cs
    Percent=Total/500*100
    print("The Percentage=",Percent)
elif (ch==3):
    c = float(input("Enter the marks in Chemistry:"))
    p = float(input("Enter the marks in Physics:"))
    m = float(input("Enter the marks in Maths:"))
    e = float(input("Enter the marks in English:"))
    cs=float(input("Enter the marks in Computer Science:"))
    Average=c+p+m+e+cs/5
    print("The Average=",Average)
elif (ch==4):
    a=input("Enter the PARA:")
    a=a.replace("The","A")
    print("",a)
else:
    print("Wrong choice")



