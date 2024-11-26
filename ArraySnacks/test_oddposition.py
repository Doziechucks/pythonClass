from unittest import TestCase
import oddposition

class ReturningOddList(TestCase):
   def test_if_function_exist(self):
      input = [1, 9, 4, 7]
      oddposition.get_odd_list(input)

   def test_if_largest_is_returned(self):
      input = [1, 9, 4, 7]
      actual = oddposition.get_odd_list(input)
      expected = [1, 4]
      self.assertEquals(actual, expected)