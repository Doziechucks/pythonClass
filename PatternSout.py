print("{:11s}{:11s}{:11}{:7}".format("(a)", "(b)", "(c)", "(d)") )
for column in range(1,11,1):
   for row in range(0,column,1):
      print("*", end="")
   print()
for column in range(1,11,1):
   for row in range(11,column,-1):
      print("*", end="")
   print()
sub = "*"
for I in range (1, 10):
   print(f"{sub:>5}")