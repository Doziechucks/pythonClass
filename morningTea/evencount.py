def return_even(list):
   count = 0
   for number in list:
      if number % 2 == 0:
         count += 1
   return count 
list = [2, 4, 5, 7, 8]
print(return_even(list))

def return_even_count(list):
   
   return len([x for x in list if x % 2 == 0])
list = [2, 4, 5, 7, 8]
print(return_even_count(list))

def get_even_count(list):
   return sum([1 for number in list if number % 2 == 0])
print(return_even_count(list))