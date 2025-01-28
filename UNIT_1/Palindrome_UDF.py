def palindrome(n):
    rev=0
    temp=0
    while(n!=0):
        temp = n%10
        rev = rev*10+temp
        n//=10
    
    if(n == rev):
        print("It is a palindrome number.")
    else:
        print("It is not a palindrome number.")
    return rev

n = int(input("Enter a number."))
a = palindrome(n)
