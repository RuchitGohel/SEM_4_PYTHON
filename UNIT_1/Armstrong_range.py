
r = int(input("Enter a range."))

for i in range(1, r):
    num = i
    og = num
    rev = 0
    while(num!=0):
        temp = num%10
        rev = rev+(temp**3)
        num//=10


    if(og == rev):
        print(i)
