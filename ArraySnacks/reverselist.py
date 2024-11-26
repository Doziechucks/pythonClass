def get_reversed_list(list):
   reversedList = []
   for number in range((len(list))-1, -1, -1):
      reversedList.append(list[number])
   return reversedList
input = [1, 9, 4, 7]

print(get_reversed_list(input))

    