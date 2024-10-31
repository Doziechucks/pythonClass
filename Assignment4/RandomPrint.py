import random
randomNumber = random.randint(1, 100)
userInput = -1

while(userInput != randomNumber):
   userInput = int(input("enter a number from 1 to 100: "))
   if (userInput == randomNumber):
      print("you are correct")
   elif userInput > randomNumber:
         print("to high, try again")
   elif userInput < randomNumber:
         print("to low, try again")

 