from unittest import TestCase
import adddigit

class ReturningDigitSum(TestCase):
   def test_if_function_present(self):
      input = 192374
      adddigit.get_sum_digit(input)

   def test_if_result_is_correct(self):
      input = 192374
      actual = adddigit.get_sum_digit(input)
      expected = 26
      self.assertEqual(expected, actual)