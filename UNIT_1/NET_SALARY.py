#Write a program to enter empid, empname, and basicsalary from user and calculate HRA 10%, DA 8%,
#TA 11%, PF 12%,; find out ( gross salary = bs + hra + ta + da - pf ) if grosssal,
# date - 04-02-2025

empid = int(input("Enter your Employeed id number:"))
empname = input("Enter your name:")
bassal = int(input("Enter your basic monthly salary:"))

hra = bassal * .10
da = bassal * .08
pf = bassal * .12
ta = bassal *.11

gsal = bassal + hra + ta + da - pf
ygsal = gsal * 12
print(f"You yearly gross salary is: {ygsal}")

if(ygsal <= 400000):
    finalsal = ygsal
    print("You get no income tax deduction.")
    print(f"Your net salary is:{finalsal}")
if(ygsal > 400000 and ygsal < 800000):
    finalsal = ygsal - (ygsal * .05)
    print("You get 5% income tax deduction.")
    print(f"Your net salary is:{finalsal}")
if(ygsal > 800000 and ygsal < 1200000):
    finalsal = ygsal - (ygsal * .10)
    print("You get 10% income tax deduction.")
    print(f"Your net salary is:{finalsal}")
if(ygsal > 1200000 and ygsal < 1600000):
    finalsal = ygsal - (ygsal * .15)
    print("You get 15% income tax deduction.")
    print(f"Your net salary is:{finalsal}")
if(ygsal > 1600000 and ygsal < 2000000):
    finalsal = ygsal - (ygsal * .20)
    print("You get 20% income tax deduction.")
    print(f"Your net salary is:{finalsal}")
if(ygsal > 2000000 and ygsal < 2400000):
    finalsal = ygsal - (ygsal * .25)
    print("You get 25% income tax deduction.")
    print(f"Your net salary is:{finalsal}")
if(ygsal > 2400000):
    finalsal = ygsal - (ygsal * .30)
    print("You get 30% income tax deduction.")
    print(f"Your net salary is:{finalsal}")

