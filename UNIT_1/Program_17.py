# Program - 17 Write a program to create dictionary in such a way that it should 
# add number as a key and square root of number as a value 
# between 1 to n in the dictionary... At the end, the data shall be 
# displayed.
# Example : {1:1, 2:4, 3:9, 4:16, 5:25, ...}

n = int(input("Enter ending range:"))
dict={}

for i in range(1, n+1):
    dict[i]=i**2

print(dict)
