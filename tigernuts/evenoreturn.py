list = [1, 3, 4, 6, 9]
def even_add(list):
   sum = 0
   for numbers in list:
      if numbers % 2 == 0:
         sum = sum + numbers
   return sum

print(even_add(list))