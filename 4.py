#Letter simplifier
letter='''This is to inform you that you are selected ,<Name>
           Congrats For this thing. 
             
             
            Date=<Date> '''
a=input("Enter the name:")
b=input("Enter the Date:")
letter=letter.replace("<Name>",a)
letter=letter.replace("<Date>",b)
print("",letter)

