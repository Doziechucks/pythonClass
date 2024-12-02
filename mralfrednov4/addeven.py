def add_even(list):
   sum = 0 
   for number in range(len(list)):
      if list[number] % 2 == 0:
         sum += list[number] 
   return sum