from unittest import TestCase
import double

class ReturningDoubleList(TestCase):
   def test_if_function_present(self):
      list = [1, 5, 12, 15, 8]
      double.get_double(list)

   def test_if_result_is_correct(self):
      list = [1, 5, 12, 15, 8]
      actual = double.get_double(list)
      expected = [2, 10, 24, 30, 16]
      self.assertEqual(expected, actual)