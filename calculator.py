a=int(input("Type 1 to add, 2 to subtract, 3 to multiply and 4 to divide"))
x=int(input("What is the first number"))
y=int(input("What is the second number"))
if a==1:
    c=x+y
    print(c)
elif a==2:
    c=x-y
    print(c)    
elif a==3:
    c=x*y
    print(c)
elif a==4:
    c=x/y
    print(c)