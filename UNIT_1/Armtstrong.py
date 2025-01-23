# date : 01-20-2025
# Armstrong

rev=0;
temp=0;

for i in range (0, 1001):
    
    n = int(input("Enter a number."))
    num = n
    while(n!=0):
        temp = n%10
        rev = rev+(temp*temp*temp)
        n//=10

if(num == rev):
    print(n)
else:
   print("It is not an armstrong number.")
