userInput = int(input("Enter number: "))
for column in range(1, 10):
   for row in range(10, 0, -1):
      print(" ", end=" ")
   for row in range(column, userInput, 1):
      print(row)