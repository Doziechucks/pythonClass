from unittest import TestCase
import listmanipulation

class PrintsSwitchedList(TestCase):
   def test_if_function_exixt(self):
      list = [1, 2, 3, 4, 6]
      numberIn = 2
      listmanipulation.get_switched_list(list, numberIn)

   def test_if_function_returns_accurate_result(self):
      list = [1, 2, 3, 4, 6]
      numberIn = 2
      actual = listmanipulation.get_switched_list(list, numberIn)
      expected = [3, 4, 6, 1, 2]
      self.assertEquals(expected, actual)
   