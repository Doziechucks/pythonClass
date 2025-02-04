def student_grades_return(student_scores):
   student_grades = {}
   for key, value in student_scores.items():
      if value > 90 and value <= 100:
         student_grades[key] = "outstanding"
      elif value > 81 and value <= 90:
         student_grades[key] = "Exceeds Expectations"
      elif value >= 71 and value <= 80:
         student_grades[key] = "Acceptable"
      elif value < 70:
         student_grades[key] = "Fail"
   return student_grades