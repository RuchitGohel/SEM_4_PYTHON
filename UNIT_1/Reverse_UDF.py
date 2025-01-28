def reverse(n):
    rev=0
    temp=0
    while(n!=0):
        temp = n%10
        rev = rev*10+temp
        n//=10
    print(rev)
    return rev

n = int(input("Enter a number."))
a = reverse(n)


