'''
Bitwise operator: Which operator works on single bit that means bit by bit it's
called bitwise operator.
>> Types:
    1. Bitwise AND         : &
    2. Bitwise OR          : |
    3. Bitwise Ex OR       : ^
    4. Bitwise left shift  : <<
    5. Bitwise right shift : >>
    6. Bitwise Compliment  : ~
'''
num1=int(input("Enter the first value: "))
num2=int(input("Enter the second value: "))
result = num1 & num2
print("Bitwise AND Operation between ",num1,"and ",num2,"is: ", result)

#Biswise OR
num3=int(input("Enter the first value: "))
num4=int(input("Enter the second value: "))
result1 = num1 | num2
print("Bitwise OR Operation between ",num3,"OR",num4,"is: ", result1)

#Biswise OR
num3=int(input("Enter the first value: "))
num4=int(input("Enter the second value: "))
result1 = num1 ^ num2
print("Bitwise Ex OR Operation between ",num3," EX OR ",num4,"is: ", result1)



#    6. Bitwise Compliment  : ~

num1=int(input("Enter the first value: "))
result = ~num1
print("~",num1,"= ",result)