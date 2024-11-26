userInput = input("Enter string: ")
def check_palindrome(userInput):
   for number in range(len(userInput)):
      if userInput[number] == userInput[-(number + 1)]:
         return "palindrome"
      else:
         return "not a palindrome"

print(check_palindrome(userInput))