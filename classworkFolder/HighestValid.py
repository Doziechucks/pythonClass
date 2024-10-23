highestNumber = 0
validator = 10
for number in range(0, validator , 1):
   print("enter a number: ", end=" ")
   newNumber = int(input())
   if newNumber>0  and newNumber <= 100:
      if highestNumber < newNumber:
         highestNumber = newNumber

   else:
      print("invalid input")
      validator = validator -1  
print("highest number is: ", highestNumber)
   