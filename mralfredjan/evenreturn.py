def even_return(userInput):
   even_list = []
   for alphabet in userInput:
      if alphabet.isdigit() == True:
         man = int(alphabet)
         if man % 2 == 0:
            even_list.append(man)
   return even_list

def square_output(numberInput):
   square_dict = {}
   square_dict[1] = numberInput
   square_dict[2] = numberInput ** 2
   return square_dict