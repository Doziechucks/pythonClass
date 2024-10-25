integerInput = int(input("Enter a decimal number: "))
reverseBinary = " "
while integerInput != 0:
   binary = integerInput % 2
   reverseBinary = str(binary) + reverseBinary 
   integerInput = integerInput // 2
print(reverseBinary)
   