#maximim number of 3 types
a=int(input("enter your first number : "))
b=int(input("enter your second number : "))
c=int(input("enter your third number : "))
if (a>b) and (a>c):
    print("maximam number is",a)

elif (b>a) and (b>c):
    print("maximum number is",b)

else:
    print("maximam number is", c)