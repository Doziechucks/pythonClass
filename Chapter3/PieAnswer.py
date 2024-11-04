x = 3
count =  0
pie = 4
while count < 150000:
   pie = pie - 4/(x) 
   if x > 0:
      x = (x + 2) * -1
   else:
      x = (x * -1) + 2
   count = count + 1
   print(pie)
   