from random import randint

correct = 0
sign = "+"
answer = 0
for number in range(10):
   first_number = randint(0, 20)
   second_number = randint(0, 20)
   number_rand = randint(0, 4)
   
   x = 1
   while(x == 1):
      try:
         if number_rand == 0:
            sign = "+" 
            answer = first_number + second_number 
         if number_rand == 1:
            sign = "-" 
            answer = first_number - second_number 
         if number_rand == 2:
            sign = "*"  
            answer = first_number * second_number 
         if number_rand == 3:
            sign = "/"
            answer = first_number / second_number

         user_input = float(input(f"{first_number} {sign} {second_number} =  "))
         print(f"your answer is: {user_input} ")
 
         if round(answer, 2) == user_input:
            print("Correct")
            correct = correct + 1
         else:
            print("Incorrect")
            print(f"correct answer is: {answer:f}")
         x = 0
      except ValueError:
         print("Invalid input")
      
      


print(f"{correct}/10")
   