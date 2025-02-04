
def uniques(list):
   list_return = {}
   frequency = 0
   for position in list:
      number = str(position) 
      if number in list_return:
         values = list_return.get(number) + 1
         list_return[number] = values

      if number not in list_return:
         list_return[number] = 1
         
   return list_return
         
print(uniques([1, 2, 4, 2, 3, 1, 3, 2, 2, 2]))