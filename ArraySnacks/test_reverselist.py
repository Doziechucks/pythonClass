from unittest import TestCase
import reverselist

class ReturningReverse(TestCase):
   def test_if_function_exist(self):
      input = [1, 9, 4, 7]
      reverselist.get_reversed_list(input)

   def test_if_largest_is_returned(self):
      input = [1, 9, 4, 7]
      actual = reverselist.get_reversed_list(input)
      expected = [7, 4, 9, 1]
      self.assertEquals(actual, expected)