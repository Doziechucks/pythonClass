import math
numberOfSides = int(input("Enter the number of side: "))
lengthOfSide = int(input("enter the length of a side: "))

areaOfPolygon = (numberOfSides * (lengthOfSide ** 2)) / (4 * math.tan(3.142/numberOfSides))
print(f"the area of the polygon is {areaOfPolygon}")