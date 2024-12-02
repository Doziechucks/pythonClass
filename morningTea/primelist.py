def return_prime_list(input):
   primeList = []
   counter = 0
   count = 0
   for number in range(1, input):
      for integer in range(1, number):
         if number % integer == 0:
            count += 1
     
      if count == 1:
         primeList.append(number)
      count = 0
         
   return primeList
input = int(input("enter no: "))
print(return_prime_list(input))