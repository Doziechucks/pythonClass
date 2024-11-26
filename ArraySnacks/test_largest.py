from unittest import TestCase
import largest

class ReturningHighest(TestCase):
   def test_if_function_exist(self):
      input = [1, 9, 4, 7]
      largest.get_largest(input)

   def test_if_largest_is_returned(self):
      input = [1, 9, 4, 7]
      actual = largest.get_largest(input)
      expected = 9
      self.assertEquals(actual, expected)