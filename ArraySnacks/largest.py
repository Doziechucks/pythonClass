def get_largest(list):
   largest = list[0]
   for number in range(len(list)):
      if list[number] > largest:
         largest = list[number]
   return largest

input = [1, 9, 4, 7]
print(get_largest(input)) 