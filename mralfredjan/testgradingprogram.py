from unittest import TestCase
import gradingprogram

class ReturningGrades(TestCase):
   def test_if_function_student_grades_return_present(self):
      student_scores = {"Gloria": 88, "divine": 75, "Esther": 65, "Mercy": 75, "Uzo": 71}
      gradingprogram.student_grades_return(student_scores)

   def test_if_function_can_return_correct_range(self):
      student_scores = {"Gloria": 88, "divine": 75, "Esther": 65, "Mercy": 75, "Uzo": 71}
      actual = gradingprogram.student_grades_return(student_scores)
      expected = {"Gloria": "Exceeds Expectations", "divine": "Acceptable", "Esther": "Fail", "Mercy": "Acceptable", "Uzo": "Acceptable"}
      self.assertEqual(actual, expected)