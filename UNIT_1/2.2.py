age = int(input("Enter your age"))

if(age < 12):
    print("You are kid")
elif(age > 12 and age < 17):
    print("You are a teenager")
elif(age > 18 and age < 60):
    print("You are adult")
else:
    print("Senior citizen")
