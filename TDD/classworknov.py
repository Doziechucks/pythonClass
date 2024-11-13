import math
def divide_or_square(number):
   if type(number) in [int, float]:
      numbers = abs(number)
      if numbers % 5 == 0:
         squareR = round(math.sqrt(numbers), 2)
         if number < 0:
            return f"j{squareR}"
         else:  
            return squareR    
      else:
        return round((number % 5), 1)
     
   raise TypeError




   