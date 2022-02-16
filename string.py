#Printing even no. of strings

a=input("Enter the string:")
b=len(a)
for i in range(0,b,2):
       if i%2==0:
               print(a[i] ,"" ,  sep="," , end="")






a=input("Enter the str:")
print("The string in reverse order is:",a)
b=len(a)
for i in range(-1,-b-1,-1):
           print(a[i] ,  end="")
