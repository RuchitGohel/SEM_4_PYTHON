p = float(input("Enter principal amount."))
r = float(input("Enter rate of interest"))
t = float(input("Enter time in years."))

CI = p * (1 + r/100) ** t - p
print("Prinicipal amount is :",p)
print("Interest rate is ",r)
print("Duration is: " ,t)
print("Compound interest is:", CI)
