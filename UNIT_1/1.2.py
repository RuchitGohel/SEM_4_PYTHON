#1.2 Write a program to input two numbers and an arithmetic operator from user and display result accordingly

a=int(input("Enter value 1"))
b=int(input("Enter value 2"))

op=input("Enter an arithmetic operator")

if op=='+':
    print("Addition is", a+b)
elif op=='-':
    print("Subtraction is", a-b)
elif op=='/':
    print("Division is", a/b)
elif op=='*':
    print("Multiplication is", a*b)
else:
    print("Invalid input")
