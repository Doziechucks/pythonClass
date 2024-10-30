userInput = int(input("enter a number: "))
summation = userInput
quitter = 0
while(quitter != -1):
   userInput = int(input("enter another number: "))
   summation = summation + userInput
   print(f"sum is: {summation}")
   quitter = int(input("Enter -1 to quit else press any other number: "))
print(f"the sum of the numbers is {summation}")
   