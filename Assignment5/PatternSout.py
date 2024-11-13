print("(a)")
for column in range(1,11):
   for row in range(1,(column + 1)):
      print("*", end="") 
   print()
print("(b)")
for column in range(1,11):
   for row in range(11,(column), -1):
      print("*", end="") 
   print()
print("(c)")
for column in range(1,11):
   for row in range(10,column, -1):
      print(" ", end="")
   for row in range(0, column, 1):
      print("*", end="")
     
   print()
print("(d)")
for column in range(1,11):
   for row in range(1,(column)):
      print(" ", end="") 
   for row in range(10, (column-1), -1):
      print("*", end="") 

   print()