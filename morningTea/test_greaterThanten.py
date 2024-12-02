from unittest import TestCase
import greaterThanten

class ReturningGreaterThanTenList(TestCase):
   def test_if_function_present(self):
      list = [1, 5, 12, 15, 8]
      greaterThanten.get_greater_than_ten(list)

   def test_if_result_is_correct(self):
      list = [1, 5, 12, 15, 8]
      actual = greaterThanten.get_greater_than_ten(list)
      expected = [12, 15]
      self.assertEqual(expected, actual)