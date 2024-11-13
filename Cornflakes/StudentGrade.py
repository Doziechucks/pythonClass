passed = 0
failed = 0

for student in range(1, 16):
   grade = int(input("Enter grade: "))
   if (grade >= 45 and grade <= 100):
      passed += 1
      print("passed")
   elif grade >= 0 and grade < 45:
      failed += 1
      print("failed")
print(f"{passed} Students passed and {failed} student failed.")
if passed > 12:
   print("well done tutor")
else:
   print("okay")