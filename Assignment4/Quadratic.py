firstCoefficient = float(input("enter coefficient of XSquared: "))
coefficientOfX = float(input("enter coefficient of X: "))
constant = float(input("enter constant: "))

part = (coefficientOfX**2)- 4 * firstCoefficient * constant
if part >= 0:
   rootOne = -coefficientOfX + (part**(1/2)/(2 * firstCoefficient))
   rootTwo = -coefficientOfX - (part**(1/2)/(2 * firstCoefficient))
   print(f"the root of the quadratic equation is: {rootOne:.2f} and {rootTwo:.2f}")
if part < 0:
   real = -coefficientOfX/(2 * firstCoefficient)
   imagin = part * -1
   imaginary = (imagin ** (1/2))/(2 * firstCoefficient)
   print(f"the roots of the quadratic equation is: {real:.2f} + {imaginary:.2f}j and {real:.2f} - {imaginary:.2f}j")