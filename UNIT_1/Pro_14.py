#Program_14
# Write a program to print all prime numbers from 1 to 100
# 09-01-2025

flag=0

for i in range(1,101):
    if(i%2==0):
        flag=1
        break
    else:
        flag=0

if(flag==0):
    print(i)
