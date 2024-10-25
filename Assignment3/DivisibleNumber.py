lowerRange = int(input("Enter the lower range of number: "))
upperRange = int(input("Enter the upper range of number: "))
divisor = int(input("Enter the divider number: "))
numberOfTimes = 0
for number in range(lowerRange, upperRange, divisor):
   numberOfTimes = numberOfTimes + 1
print(numberOfTimes)