numberOfYears = 1
principal = 1000
annualRate = 7/100
while numberOfYears <= 30:
   amount =  principal*(1 + annualRate)**numberOfYears
   numberOfYears += 1
   print(amount)