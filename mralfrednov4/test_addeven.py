from unittest import TestCase
import addeven 

class checkeven(TestCase):
   def test_that_function_exist(self):
      list = [2, 4, 5, 7, 8]
      addeven.add_even(list)

   def test_if_function_can_return_second_value_in_a_list(self):
      list = [2, 4, 5, 7, 8]
      actual = addeven.add_even(list)
      expected = 14
      self.assertEquals(actual, expected)