def get_even_list(list):
   evenList = []
   for number in range(len(list)):
      if number % 2 == 1:
         evenList.append(list[number])
   return evenList

input = [1, 9, 4, 7]
print(get_even_list(input)) 