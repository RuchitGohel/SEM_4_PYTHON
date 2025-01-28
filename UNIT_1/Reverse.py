# date : 01-20-2025
# print reverse of a number.

rev=0;
temp=0;

n = int(input("Enter a number."))

while(n!=0):
    temp = n%10
    rev = rev*10+temp
    n//=10

print(rev)

