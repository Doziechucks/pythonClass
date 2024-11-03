summation = 0
counter = 0
product = 1
numberInput = int(input("input number: "))
largest = numberInput
smallest = numberInput
while counter < 3:
   numberInput = int(input("input number: "))
   if numberInput > largest:
      largest = numberInput
   elif numberInput < smallest:
      smallest = numberInput 
   counter += 1
   summation += numberInput
   product = product * numberInput
mean = summation / 4
print(f"the sum, mean, product, smallest and largest is {summation}, {mean}, {product}, {smallest} and {largest}")  
    