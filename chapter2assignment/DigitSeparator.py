numberInput = int(input("Enter a 5 digit number: "))
firstInteger = numberInput // 10000
fiftInteger = numberInput % 10
tosecInteger = numberInput // 1000
secondInteger = tosecInteger % 10
toThird = numberInput // 100
thirdInteger = toThird % 10
toForth = numberInput // 10
fourthInteger = toForth % 10
print(firstInteger, secondInteger, thirdInteger, fourthInteger, fiftInteger)