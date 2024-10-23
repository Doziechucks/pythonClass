highestNumber = 0
for number in range(0, 10, 1):
   print("enter a number: ", end=" ")
   newNumber = int(input())
   if newNumber <= 100:  
      if highestNumber < newNumber:
         highestNumber = newNumber
   else:
      print("invalid input")
print("highest number is: ", highestNumber)
   