def get_odd_list(list):
   oddList = []
   for number in range(len(list)):
      if number % 2 == 0:
         oddList.append(list[number])
   return oddList

input = [1, 9, 4, 7]
print(get_odd_list(input)) 