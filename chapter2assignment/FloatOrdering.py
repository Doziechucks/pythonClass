firstNum = float(input("Enter first number: "))
largest = firstNum 
smallest = firstNum
middleNum = firstNum 
secondNum = float(input("Enter second Number: "))
if secondNum > largest:
   largest = secondNum
if secondNum < smallest:
   smallest = secondNum 
thirdNum = float(input("Enter third number: "))
if thirdNum > largest:
   largest = thirdNum
if thirdNum < smallest:
   smallest = thirdNum
if largest == firstNum and smallest == secondNum:
   middleNum = thirdNum
if largest == firstNum and smallest == thirdNum:
   middleNum = secondNum
if largest == thirdNum and smallest == secondNum:
   middleNum = firstNum
if largest == thirdNum and smallest == firstNum:
   middleNum = secondNum
if largest == secondNum and smallest == firstNum:
   middleNum = thirdNum
if largest == secondNum and smallest == thirdNum:
   middleNum = firstNum
print(smallest, middleNum, largest)