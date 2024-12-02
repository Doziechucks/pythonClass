def get_first_capital(list):
   new_list = []
   for word in list:
      new_list.append(word.capitalize())
   return new_list

def capitalize_first(list):
   return[word.capitalize() for word in list]

input= ["red", "yellow", "blue", "green"]
print(capitalize_first(input))