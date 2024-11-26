from unittest import TestCase
import elementcheck

class ReturningHighest(TestCase):
   def test_if_function_exist(self):
      input = [1, 9, 4, 7]
      check = 4
      elementcheck.check_present(input, check)

   def test_if_largest_is_returned(self):
      input = [1, 9, 4, 7]
      check = 4
      actual = elementcheck.check_present(input, check)
      expected = True
      self.assertEquals(actual, expected)
      input = [1, 9, 4, 7]
      check = 2
      actual = elementcheck.check_present(input, check)
      expected = False
      self.assertEquals(actual, expected)