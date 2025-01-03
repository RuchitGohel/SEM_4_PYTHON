# input 5 subject marks from user and display result, total, grade, percentage

a = int(input("Enter marks for subject1"))
b = int(input("Enter marks for subject2"))
c = int(input("Enter marks for subject3"))
d = int(input("Enter marks for subject4"))
e = int(input("Enter marks for subject5"))

total = a+b+c+d+e
percentage= (total*100)/500

if percentage<=35:
    print("You have failed the exam")
else:
    print("You have passed!")

print("Your percentage is:",percentage)

if percentage<100 and percentage >= 90:
    print("Your grade: A")
elif percentage<90 and percentage >= 80:
    print("Your grade: B")
elif percentage<80 and percentage >= 70:
    print("Your grade: A")
elif percentage<70 and percentage >= 50:
    print("Your grade: D")
elif percentage<50 and percentage >= 35:
    print("Your grade: E")
else:
    print("Your grade: F")
