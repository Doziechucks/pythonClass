userInput = int(input("Enter number for pattern number: "))
for number in range(1, (userInput + 1)):
   for pattern in range(1, (number+1)):
      print("*", end=" ")
   print()
