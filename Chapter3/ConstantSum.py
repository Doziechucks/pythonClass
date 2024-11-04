epsilon = 1
count = 0

for number in range (1, 10, 1):
   factorial = number
   if number == 0 or number == 1:
      numberF = 1
   else:
      while number != 1:
         factorial  = (number-1) * factorial
         number -= 1
      numberF = factorial
   
   epsilon =  epsilon + (1/numberF)
print(epsilon)