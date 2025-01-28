# date: 01-20-2025
# Program - 15 Write a program to print factorial of a number using function.

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact=fact*i
    return fact

n = int(input("Enter a number."))
f = factorial(n)
print(f"Factorial of {n} is : {f}")
