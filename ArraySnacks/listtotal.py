def get_total(list):
   total = 0
   for number in range(len(list)):
      total += list[number]
   return total

input = [1, 9, 4, 7]
print(get_total(input)) 