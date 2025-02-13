def soughter(number):
   for num in range(len(number) - 1):
      for element in range(len(number) - 1):
          if number[element] > number[element + 1]:
             man = number[element + 1]
             number[element + 1] = number[element]
             number[element] = man
   return number

numbers = [1, 5, 2, -2]
print(soughter(numbers)) 