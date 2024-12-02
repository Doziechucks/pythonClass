def get_bool_list(list):
   return[True if (number % 2 == 0) else False  for number in list]
list = [1,2,4,3,6,5,7]
print(get_bool_list(list))