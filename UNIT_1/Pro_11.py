# Program-11
#09-01-2025
# Write a program to input a number and display its factorial.
# e.g. 5 = 5 * 4 * 3 * 2 * 1 = 120

number = int(input("Enter a number to know its factorial"))
factorial = 1
for i in range(1, number+1):
    factorial *= i
print(factorial)
