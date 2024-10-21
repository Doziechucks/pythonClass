principal = float(input("Enter the principal amount: "))
AnnualInterest = float(input("Enter the annual interest rate: "))
r = AnnualInterest /1200
Duration = float(input("enter the duration in years: "))
n = Duration * 12

monthlypayments = (principal * r * ((1 + r)**n))/ (((1 + r)**n) - 1 )
print(f"your monthly payment is {monthlypayments:.2f}")