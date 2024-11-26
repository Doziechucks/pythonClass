input  = [1,2,5,-5,5,2,8] 

def number_adder(number):
   summing = 0
   if type(input) is list:
      for number in range(len(input)): 
         summing += input[number]
      return summing
   
   raise TypeError("only integers and floats allowed")

   
   