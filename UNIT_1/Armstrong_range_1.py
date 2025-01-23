
r = int(input("Enter a range."))

#digits = len(str(num))
for i in range(1, r):
    num = i
    og = num
    digits = 0
    while(og!=0):
        og = og//10
        digits+=1

    s=0
    current=0

    number = num

    while num > 0:
        current = (num % 10)
        s+=(current**digits)
        num = num//10

    if s==number:
        print(number)
