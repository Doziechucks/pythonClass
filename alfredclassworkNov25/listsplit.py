def get_split_list(list):
   listOne = []
   listTwo = []
   listOga = []
   number = 0
   if len(list) % 2 == 0:
      number = len(list) // 2
   else:
      number = (len(list) // 2) + 1
   for count in range(number):
      listOne.append(list[count])
   for count in range(number, len(list)):
      listTwo.append(list[count])
   listOga.append(listOne)
   listOga.append(listTwo)

   return listOga

listInput = [1, 2, 3, 4, 6, 7, 9]
print(get_split_list(listInput))
