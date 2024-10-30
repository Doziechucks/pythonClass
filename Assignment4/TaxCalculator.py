userSalary = float(input("Enter your salary: "))
if userSalary > 30000:
   taxPay = userSalary * 0.2
else:
   userSalary * 0.15
print(f"the tax you are to pay is: {taxPay}")