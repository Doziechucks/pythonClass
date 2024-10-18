numberR = int(input("Enter 3 digit number: "))
firstD = numberR //100
thirdD = numberR % 10
toSec = numberR // 10
SecondD = toSec % 10
print(thirdD, SecondD, firstD)
evenN = 0
oddN = 0
if firstD % 2 == 0:
   evenN = evenN + 1
else:
   oddN = oddN + 1
if SecondD % 2 == 0:
   evenN = evenN + 1
else:
   oddN = oddN + 1     
if thirdD % 2 == 0:
   evenN = evenN + 1
else:
   oddN = oddN + 1
print("even is: ",evenN )
print("and odd is: ", oddN)