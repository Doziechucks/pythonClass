negNumbers = 0
posNumber = 0
zeroNumber = 0
for number in range(0, 5, 1):
   newNumber = int(input("Enter an integer: "))
   if newNumber < 0:
      negNumbers = negNumbers + 1
   if newNumber > 0:
      posNumber = posNumber + 1
   if newNumber == 0:
      zeroNumber = zeroNumber + 1
print(f"the number of positive, negative, and zero number is: {posNumber}, {negNumbers}, {zeroNumber}")   
   