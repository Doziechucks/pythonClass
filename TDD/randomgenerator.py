from random import randint
addition = []

def RandomQuestions():
   addition = []
   correct = 0
   fail = 0
   for number in range(5):
      number1 = randint(1, 1000)
      number2 = randint(1, 1000)
      answer = int(input(f"{number1} + {number2} = "))
      adder = f"{number + 1}. {number1} + {number2} = {number1 + number2}"
      if answer == number1 + number2:
         correct += 1
      else:
         fail += 1
         addition.append(adder)

   for number in range(3):
      number1 = randint(1, 1000)
      number2 = randint(1, 1000)
      answer = int(input(f"{number1} x {number2} = "))
      adder = f"{number + 6}. {number1} x {number2} = {number1 * number2}"
      if answer == number1 * number2:
         correct += 1
      else:
         fail +=1
         addition.append(adder)
   for number in range(2):
      number1 = randint(1, 1000)
      number2 = randint(1, 1000)
      answer = int(input(f"{number1} - {number2} = "))
      adder = f"{number + 9}. {number1} - {number2} = {number1 - number2}"
      if answer == number1 - number2:
         correct += 1
      else:
         fail +=1
         addition.append(adder)
   print("your failed questions with their answers are: ")
   for number in range(len(addition)):
      print(addition[number])
   total = fail + correct
   print(f"your score is {correct} / {total}")
RandomQuestions()