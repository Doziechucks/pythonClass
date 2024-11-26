def check_present(list, element):
   for number in range(len(list)):
      if list[number] == element:
         return True
   else:
      return False

input = [1, 9, 4, 7]
check = 4
print(check_present(input, check))
   