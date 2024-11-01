userInputOne = int(input("enter first number: "))
userInputtwo = int(input("enter first number: "))
userInputThree = int(input("enter first number: "))

if(userInputtwo > userInputOne and userInputThree > userInputtwo):
   print("ascending order")
elif(userInputtwo < userInputOne and userInputThree < userInputtwo):
   print("descending order")
else:
   print("can not determine trend")