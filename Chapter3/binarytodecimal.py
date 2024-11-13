binaryNumber = int(input("input binary number: "))
multiplier = 1
decimalNumber = 0
while(binaryNumber > 0):
   binary =  binaryNumber % 10
   decimal = binary * multiplier
   binaryNumber = binaryNumber // 10
   multiplier = multiplier * 2
   decimalNumber = decimalNumber + decimal
print(decimalNumber)