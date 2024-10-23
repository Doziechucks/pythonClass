
firstNum = int(input("Enter first number: "))
largest = firstNum 
smallest = firstNum
secondNum = int(input("Enter second Number: "))
if secondNum > largest:
   largest = secondNum
if secondNum < smallest:
   smallest = secondNum 
thirdNum = int(input("Enter third number: "))
if thirdNum > largest:
   largest = thirdNum
if thirdNum < smallest:
   smallest = thirdNum
summation = firstNum + secondNum + thirdNum
average = (firstNum + secondNum + thirdNum) / 3
product = (firstNum * secondNum * thirdNum)
print(f"the sum, product, average, smallest and largest is: {summation}, {product}, {average}, {smallest} and {largest}")