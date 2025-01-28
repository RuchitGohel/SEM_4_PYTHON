# date : 28-01-2025
# Armstrong using udf

def Armstrong(n):
    og = n
    rev = 0
    temp = 0
    while(n!=0):
        temp = n%10
        rev = rev+(temp**3)
        n//=10

    if(rev == og):
        print("It is an armstrong number.")
    else:
        print("It is not an armstrong number.")
    return rev

n = int(input("Enter a number:"))
a = Armstrong(n)
