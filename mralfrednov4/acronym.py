uInput = input("Enter a sentence: ")
userInput = uInput.title()
print(userInput)

def acronym_making(sentence):
   count = ""
   for letter in userInput:
      variable = letter.upper()
      if variable == letter:
         count = count + f"{letter}".strip()  
   return count

print(acronym_making(userInput))
      
     