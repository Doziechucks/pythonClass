from random import randint
variableOne = randint(1, 100)
variableTwo = randint(1, 100)
summation = variableOne + variableTwo
userInput = int(input(f"{variableOne} + {variableTwo}: "))
if userInput == summation:
   print(True)
else:
   print(False)