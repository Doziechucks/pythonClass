from unittest import TestCase
import stringlist

class ReturningGreaterThanTenList(TestCase):
   def test_if_function_present(self):
      list = ["Apple", "fish", "Orange", "ice", "lime"]
      stringlist.get_string_list(list)

   def test_if_result_is_correct(self):
      list = ["Apple", "fish", "Apple", "ice", "lime"]
      actual = stringlist.get_string_list(list)
      expected = ["Apple", "Apple"]
      self.assertEqual(expected, actual)