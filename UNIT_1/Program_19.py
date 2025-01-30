# Program-19 : Write a Python Program to create a function which accepts 3
# arguments. (2 numbers and one arithmetic operator). Display
# answer accordingly
# date : 29-01-2025

def Arith(num1,num2,op):
    if op=="+":
        return num1+num2
    if op=='-':
        return num1-num2
    if op=='*':
        return num1*num2
    if op=='/':
        return num1/num2
    if op=='%':
        return num1%num2


n1= int(input("Enter Number 1:"))
n2= int(input("Enter Number 1:"))
o= input("Enter Operator:")

print(Arith(n1,n2,o))

