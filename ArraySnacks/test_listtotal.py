from unittest import TestCase
import listtotal

class ReturningTotal(TestCase):
   def test_if_function_exist(self):
      input = [1, 9, 4, 7]
      listtotal.get_total(input)

   def test_if_list_total_correct(self):
      input = [1, 9, 4, 7]
      actual = listtotal.get_total(input)
      expected = 21
      self.assertEquals(actual, expected)