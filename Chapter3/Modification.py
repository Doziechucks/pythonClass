userInput = 0
counter = 0
while userInput not in ("1", "2"):
   userInput = input("Enter a number: ")
   counter = counter + 1
print(f"you tried {counter}times")