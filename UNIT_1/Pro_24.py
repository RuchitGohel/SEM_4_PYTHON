# 18-02-2025
# Prog - 24: Write a Python Program that creates a class with function 
# overloading

class Calculator:
    def addition(self, *args):
        return sum(args)

c = Calculator()
print(c.addition(5))
print(c.addition(5, 10))
print(c.addition(5, 10, 15))
print(c.addition(5, 101, 15, 20))
