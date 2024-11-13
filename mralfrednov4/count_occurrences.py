userInput = input("Enter a word: ")
chosen = input("Enter letter to check: ")
def counting_occurrence(letter, word):
   count = 0
   for letter in userInput:
      if letter == chosen:
         count += 1 
   return count 
 
print(counting_occurrence(userInput, chosen))