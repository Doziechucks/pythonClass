integerAdder = int(input("Enter an integer between 0 to 1000: "))
firstDigit = integerAdder // 100
tosec = integerAdder // 10
secondDigit = tosec % 10
thirdDigit = integerAdder % 10 
summation = firstDigit + secondDigit + thirdDigit
print(f"the summation of the integer id {summation}")