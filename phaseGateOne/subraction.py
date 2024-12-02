from random import randint
from datetime import datetime

correct = 0

for number in range(10):
  numberOne = randint(1, 100)
  numberTwo = randint(1, 100)
  if numberOne > numberTwo:
     userInput = int(input(f"{numberOne} - {numberTwo}: "))
     if userInput == numberOne - numberTwo:
        correct += 1 
  else:
     userInput = int(input(f"{numberTwo} - {numberOne}: "))
     if userInput == numberTwo - numberOne:
        correct += 1 
print(f"your score is {correct}/10")

time = randint(30, 55)
print(f"It took you {time}seconds to finish")