userInput1 = int(input("Enter integer: "))
userInput = userInput1
factorial = userInput
if userInput == 0 or userInput == 1:
   print(f"{userInput1}! = 1")
else:
   while userInput != 1:
      factorial  = (userInput-1) * factorial
      userInput -= 1
   print(f"{userInput1}! is {factorial}")