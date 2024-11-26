list = [1, 2, 3, 4, 5]
def add_complex(list):
   sum = 0
   for number in range(len(list)):
      for numb in range(len(list)):
         if number != numb:
            sum += list[number]
   return sum

print(add_complex(list))

