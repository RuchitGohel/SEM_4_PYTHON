s1 = ("Enter marks of s1")
s2 = ("Enter marks of s2")
s3 = ("Enter marks of s3")
s4 = ("Enter marks of s4")

total = s1 + s2 + s3 + s4 + s5

perc = (total*100)/500

print(f"Toal is : {total}")
print(f"Percentage is: {perc}")

if(s1 >= 40 and s2 >= 40 and s3 >= 40 and s4 >= 40):
    print("result: pass")
    if(per>70):
        peint("Grade : A")
    elif(per>=60 and per<70):
        print("Grade : B")
    elif(per>=50 and per<60):
        print("Grade : C")
    elif(per>=40 and per<50):
        print("Grade : B")
    else:
        print("Result : fail")
        print("Grade: ****")
