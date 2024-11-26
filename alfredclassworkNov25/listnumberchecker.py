def check_for_even(input):
   output = []
   for number in range(len(input)):
      if input[number] % 2 == 0:
         output.append(True)
      else:
         output.append(False)
   return output
list = [1, 3, 5, 6, 8, 4]
print(check_for_even(list))
