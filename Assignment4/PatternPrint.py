print("Pattern A")
for column in range(1,7,1):
   for row in range(0,column,1):
      print("*", end=" ")
   print()
print("Pattern B")
for column in range(1,7,1):
   for row in range(7,column,-1):
      print("*", end=" ")
   print()