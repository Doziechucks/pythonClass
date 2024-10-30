userInput = int(input("Enter integer value: "))
for multiplier in range(0, (userInput + 1), 1):
   product = userInput * multiplier
   print(f"{userInput} x {multiplier} = {product}")
   
   