userInput = int(input("Enter 5 digit number: "))
firstDigit = userInput // 10000
lastDigit = userInput % 10
tosec = userInput // 1000
secondDigit = tosec % 10
tofour = userInput % 100
forthDigit = tofour // 10
if firstDigit == lastDigit and secondDigit == forthDigit:
   print(f"{userInput} is a palindrome number")
else:
   print(f"{userInput} is not a palindrome number")