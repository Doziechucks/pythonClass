print("sideOne  sideTwo hypotenuse")
for sideOne in range(1, 21):
   for sideTwo in range (1, 21):
      for hypotenuse in range(1, 21):
         if (sideOne**2) + (sideTwo**2) == (hypotenuse**2):
            print(f"{sideOne:>7} {sideTwo:>8} {hypotenuse:>9}")