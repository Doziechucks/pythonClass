from unittest import TestCase
import evenposition

class ReturningOddList(TestCase):
   def test_if_function_exist(self):
      input = [1, 9, 4, 7]
      evenposition.get_even_list(input)

   def test_if_largest_is_returned(self):
      input = [1, 9, 4, 7]
      actual = evenposition.get_even_list(input)
      expected = [9, 7]
      self.assertEquals(actual, expected)