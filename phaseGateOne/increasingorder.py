firstNumber = int(input("enter first number: "))
largest = firstNumber
least = firstNumber
middleNumber = firstNumber
secondNumber = int(input("enter second number: "))
if secondNumber > largest:
   largest = secondNumber
if secondNumber < largest:
   least = secondNumber
thirdNumber = int(input("enter third number: "))
if thirdNumber > largest:
   largest = thirdNumber
if thirdNumber < largest:
   least = thirdNumber
if largest == firstNumber and least == secondNumber:
   middleNumber = thirdNumber
if largest == thirdNumber and least == secondNumber:
   middleNumber = firstNumber
if largest == firstNumber and least == thirdNumber:
   middleNumber = secondNumber
if largest == secondNumber and least == firstNumber:
   middleNumber = thirdNumber
if largest == thirdNumber and least == firstNumber:
   middleNumber = secondNumber
if largest == secondNumber and least == thirdNumber:
   middleNumber = firstNumber
print(f"{least}, {middleNumber}, {largest}")