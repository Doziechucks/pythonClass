quitter = 0
userInputOne = int(input("Enter first number: "))
largest = userInputOne
lowest = userInputOne
while (quitter != -1):
   userInputTwo = int(input("Enter another number: "))
   if userInputTwo > largest:
      largest = userInputTwo
   if userInputTwo < lowest:
      lowest = userInputTwo
   quitter = int(input("Enter -1 to quit or any number to continue: "))
print(f"largest is {largest} and lowest number is {lowest}")