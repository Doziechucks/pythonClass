userInput = int(input("Enter integer: "))
def check_prime(userInput):
   counter = 0
   for number in range(userInput):
      if userInput % (number + 1) == 0:
         counter += 1
   if counter > 2:
      return "not a prime"
   else:
      return "prime" 
print(check_prime(userInput))