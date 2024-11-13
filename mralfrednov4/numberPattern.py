userInput = int(input("Enter a number: "))

for column in range(0, userInput):
   for row in range(1, column + 2):
      print(row, end=" ")
   print()