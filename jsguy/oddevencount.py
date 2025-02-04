def odd_even_count(number_list):
   numbers = []
   even_count = 0
   odd_count = 0
   for number in number_list:
      if number % 2 == 0:
         even_count += 1
      else:
         odd_count += 1
   numbers.append(odd_count)
   numbers.append(even_count) 
   return numbers