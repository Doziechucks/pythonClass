upperRange = int(input("enter the upper range of value: "))
lowerRange = int(input("enter lower range of value: "))
divisor = int(input("Enter dividing number: "))
counter = 0
for divisor in range(lowerRange, upperRange, divisor):
   counter += 1
print(counter)
   