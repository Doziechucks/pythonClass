from random import randint
addition = []

def RandomQuestions():
   addition = []
   correct = 0
   fail = 0
   for number in range(5):
      number1 = randint(1, 1000)
      number2 = randint(1, 1000)
      print(f"{number1} + {number2} = ")
      answer = input()
      adder = f"{number1} + {number2} = {number + number2}"
      if answer == number1 + number2:
         correct += 1
      else:
         fail += 1
      addition.append(adder)

   for number in range(3):
      number1 = randint(1, 1000)
      number2 = randint(1, 1000)
      print(f"{number1} x {number2} = ")
      answer = input()
      adder = f"{number1} x {number2} = {number * number2}"
      if answer == number1 * number2:
         correct += 1
      else:
         fail +=1
      addition.append(adder)
   for number in range(2):
      number1 = randint(1, 1000)
      number2 = randint(1, 1000)
      print(f"{number1} - {number2} = ")
      answer = input()
      adder = f"{number1} - {number2} = {number - number2}"
      if answer == number1 - number2:
         correct += 1
      else:
         fail +=1
      addition.append(adder)
   for number in range(addition.length-1):
      print(question[number])

RandomQuestions()