wordInput = input("Enter word to be checked: ")
characterInput = input("Input character to check for: ")
wordList = ['m', 'a', 'n', 'g', 'o']
for word in wordInput:
   if characterInput == word:
      print("True")
      break;

for word in range(len(wordList)):
   if characterInput == wordList[word]:
      print(True)
      break;