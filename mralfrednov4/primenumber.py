count = 0
checker = 1
def prime number(number):
   for number in range(1, userInput):
      if number != 1:
         checker = userInput % number 
         if checker == 0:
            count = count + 1
         else:
            count = count 
      elif number == 1:
         checker = userInput % (number + 1) 
         if checker == 0:
            count = count + 1
   if count == 0:
      print("number is a prime")
   elif count > 0 :
      print("is not a prime") 
number = userInput = int(input("Enter a prime number: "))
primenumber(number)