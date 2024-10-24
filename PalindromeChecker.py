numberInput = int(input("Enter three digit Number: "))
firstInteger = numberInput // 100
lastInteger = numberInput % 5
if firstInteger == lastInteger:
   print("Entered number is a Palindrome")
else:
   print("Entered number is not a Palindrome")