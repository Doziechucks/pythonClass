import math
latitudeX1 = float(input("input the latitude of coordinate 1: "))
longitudeY1= float(input("input the  of longitude coordinate 1: "))
latitudeX2 = float(input("input the latitude of coordinate 2: "))
longitudeY2 = float(input("input the longitude of coordinate 2: "))
radius = 6371.01

distance = radius * math.acos(math.sin(math.radians(latitudeX1)) * math.sin(math.radians(latitudeX2)) + math.cos(math.radians(latitudeX1)) * math.cos(math.radians(latitudeX2)) * math.cos(math.radians(longitudeY1-longitudeY2)))

print(f"the distance between those points is: {distance}")