firstNumber = int(input("Enter first number: "))
SecondNumber = int(input("Enter second number: "))

def find_product(firstNumber, secondNumber):
   product = 0
   
   if secondNumber == 0:
      product = 0
   elif (firstNumber < 0 and secondNumber < 0):
      firstNumber = firstNumber -(firstNumber + firstNumber)
      secondNumber = secondNumber -(secondNumber + secondNumber)
   for number in range(secondNumber):
      product = product + firstNumber
      
   return product

 