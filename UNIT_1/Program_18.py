# Program -18
#Write a program which accepts a sequence of comma-separated 
#numbers from console and generate a list and a tuple which 
#contains every number
# date : 29-01-2025

n = input("Enter comma-seperated number:")

lst = n.split(",")
tup = tuple(lst)

print(lst)
print(tup)
