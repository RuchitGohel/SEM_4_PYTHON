# date : 01-20-2025
# Palindrome

rev=0;
temp=0;

n = int(input("Enter a number."))

while(n!=0):
    temp = n%10
    rev = rev*10+temp
    n//=10

if(n == rev):
    print("It is a palindrome number.")
else:
    print("It is not a palindrome number.")

