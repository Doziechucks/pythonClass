userInput = int(input("Enter a set of numbers: "))
newNum = 0
while(userInput // 10 != 0):
   Number = userInput % 10
   newNum = newNum + Number 
   userInput = userInput // 10  
print(newNum)