#Program_12
# Write a program to input a number and find out if it is prime
#09-01-2025

n=int(input("Enter a number"))
flag=0
for i in range(2,n):
    if(n%i==0):
        flag=1
        break
    
if(flag==1):
    print("It is not a prime number")
else:
    print("It is a prime number")
        

    
    
