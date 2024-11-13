userInput = input("Enter a word: ")

def vowel_checking(word):
   count = 0
   for letters in userInput:
      if letters.lower() == "a" or letters.lower() == "e" or letters.lower() == "i" or letters.lower() == "o" or letters.lower() == "u":
         count = count + 1
   return count
   



print(vowel_checking(userInput))

