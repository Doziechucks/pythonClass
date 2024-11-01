userInput = int(input("Enter a set of numbers: "))
newNum = 0
while(userInput // 10 != 0):
   number = userInput % 10
   if number > 4:
      newNum = newNum + 1
   userInput = userInput // 10
print(newNum)