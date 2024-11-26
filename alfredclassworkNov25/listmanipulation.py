def get_switched_list(list, numberInput):
   listTwo = []
   for count in range(numberInput, len(list)):
      listTwo.append(list[count])
   for count in range(numberInput):
      listTwo.append(list[count])

   return listTwo

list = [1, 2, 3, 4, 6]
numberIn = 2
print(get_switched_list(list, numberIn))