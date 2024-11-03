gallonsUsed = 0
summation = 0
count = 0
while gallonsUsed != -1:
   gallonsUsed = int(input("Enter the gallons used(-1 to quit): "))
   if gallonsUsed == -1:
      break
   milesDriven = int(input("Enter the miles driven: "))
   miles_gallon = milesDriven / gallonsUsed
   print(f"the miles/gallon for the trip is: {miles_gallon}")
   summation += miles_gallon
   count += 1
average = summation / count
print(f"the overall average miles per gallon is {average}")